%define version 1.6.4
%define name enscript
%define prefix %{_prefix}
%define release %mkrel 8

Name: %{name}
Summary: Converts plain ASCII to PostScript
Release: %{release}
Version: %{version}
License: GPL
Group: Publishing
Source0: http://www.iki.fi/mtr/genscript/enscript-%{version}.tar.gz
Patch0: enscript-1.6.4-CAN-2004-1184.patch
Patch1: enscript-1.6.1-CAN-2004-1185.patch
Patch2: enscript-1.6.1-CAN-2004-1186.patch
Patch3: enscript-rh-CVE-2008-3863+CVE-2008-4306.patch
URL: http://people.ssh.fi/mtr/genscript/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: flex gettext
Requires(post): info-install
Requires(preun): info-install
Obsoletes: nenscript
Provides: nenscript

%description
GNU enscript is a free replacement for Adobe's Enscript program. Enscript
converts ASCII files to PostScript(TM) and spools generated PostScript
output to the specified printer or saves it to a file. Enscript can be
extended to handle different output media and includes many options for
customizing printouts.

%prep
%setup -q
%patch0 -p1 -b .can-2004-1184
%patch1 -p0 -b .can-2004-1185
%patch2 -p1 -b .can-2004-1186
%patch3 -p0 -b .cve-2008-3863_4306

%build
%configure2_5x --with-media=Letter
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

mkdir -p $RPM_BUILD_ROOT/etc/%{name}
cp $RPM_BUILD_ROOT/%{_datadir}/%{name}/afm/font.map $RPM_BUILD_ROOT/etc/%{name}/font.map
pushd $RPM_BUILD_ROOT/%{_datadir}/%{name}
ln -sf /etc/%{name}/font.map
popd

rm -f $RPM_BUILD_ROOT/%{_datadir}/%{name}/font.map

%find_lang %name

# XXX note doubled %% in sed script below.
(cd %{buildroot};find .%{_datadir}/enscript/* -type f) | \
	sed -e 's,^\.,,' | sed -e 's,*font.map,%%config &,' > share.list

( cd %{buildroot}
  ln .%{_prefix}/bin/enscript .%{_prefix}/bin/nenscript
)

cat share.list >> %{name}.lang

%post
%_install_info %{name}.info

%preun
%_remove_install_info %{name}.info

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root)
%doc AUTHORS ChangeLog NEWS README README.ESCAPES THANKS TODO 
%config(noreplace) %{_sysconfdir}/enscript.cfg
%dir %{_sysconfdir}/enscript
%config(noreplace) %{_sysconfdir}/enscript/font.map
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/hl
%dir %{_datadir}/%{name}/afm
%{_bindir}/*
%{_mandir}/*/*
%{_infodir}/%{name}*


