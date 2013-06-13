Summary:	Converts plain ASCII to PostScript
Name:		enscript
Version:	1.6.6
Release:	1
License:	GPLv3
Group:		Publishing
Url:		ftp://ftp.gnu.org/gnu/enscript/
Source0:	ftp://ftp.gnu.org/gnu/enscript/%{name}-%{version}.tar.gz
BuildRequires:	flex
BuildRequires:	gettext

%description
GNU enscript is a free replacement for Adobe's Enscript program. Enscript
converts ASCII files to PostScript(TM) and spools generated PostScript
output to the specified printer or saves it to a file. Enscript can be
extended to handle different output media and includes many options for
customizing printouts.

%prep
%setup -q

%build
%configure2_5x --with-media=Letter
%make

%install
%makeinstall

mkdir -p %{buildroot}/etc/%{name}
cp %{buildroot}/%{_datadir}/%{name}/afm/font.map %{buildroot}/etc/%{name}/font.map
pushd %{buildroot}/%{_datadir}/%{name}
ln -sf /etc/%{name}/font.map
popd

rm -f %{buildroot}/%{_datadir}/%{name}/font.map

%find_lang %{name}

# XXX note doubled %% in sed script below.
(cd %{buildroot};find .%{_datadir}/enscript/* -type f) | \
	sed -e 's,^\.,,' | sed -e 's,*font.map,%%config &,' > share.list

( cd %{buildroot}
  ln .%{_prefix}/bin/enscript .%{_prefix}/bin/nenscript
)

cat share.list >> %{name}.lang

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS README README.ESCAPES THANKS TODO 
%config(noreplace) %{_sysconfdir}/enscript.cfg
%dir %{_sysconfdir}/enscript
%config(noreplace) %{_sysconfdir}/enscript/font.map
%{_bindir}/*
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/hl
%dir %{_datadir}/%{name}/afm
%{_mandir}/*/*
%{_infodir}/%{name}*

