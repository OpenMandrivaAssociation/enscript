%define	version	1.6.5.2
%define name	enscript
%define release	 4

Name:		%{name}
Summary:	Converts plain ASCII to PostScript
Release:	%{release}
Version:	%{version}
License:	GPLv3
Group:		Publishing
Source0:	ftp://ftp.gnu.org/gnu/enscript/%{name}-%{version}.tar.gz
URL:		ftp://ftp.gnu.org/gnu/enscript/
BuildRequires:	flex gettext
Obsoletes:	nenscript
Provides: 	nenscript

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




%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 1.6.5.2-2mdv2011.0
+ Revision: 664146
- mass rebuild

* Tue Nov 23 2010 Eugeni Dodonov <eugeni@mandriva.com> 1.6.5.2-1mdv2011.0
+ Revision: 600267
- Updated to 1.6.5.2.

* Sun Mar 07 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.6.5.1-1mdv2010.1
+ Revision: 515465
- fix: url, source, license, and mix use spaces/tabs in spec.
- update to 1.6.5.1
- drop old patches, not needed because applied upstream.

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.6.4-10mdv2010.0
+ Revision: 424386
- rebuild

* Sat Jan 10 2009 Funda Wang <fwang@mandriva.org> 1.6.4-9mdv2009.1
+ Revision: 327898
- P3: security fix for CVE-2008-3863 and CVE-2008-4306

* Mon Dec 29 2008 Oden Eriksson <oeriksson@mandriva.com> 1.6.4-8mdv2009.1
+ Revision: 321099
- fix url
- rediffed some fuzzy patches

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.6.4-8mdv2009.0
+ Revision: 220725
- rebuild

* Sat Jan 12 2008 Thierry Vignaud <tv@mandriva.org> 1.6.4-7mdv2008.1
+ Revision: 149698
- rebuild
- kill re-definition of %%buildroot on Pixel's request
- fix summary-ended-with-dot

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Aug 23 2007 Thierry Vignaud <tv@mandriva.org> 1.6.4-6mdv2008.0
+ Revision: 70212
- convert prereq


* Sat Jan 27 2007 Gustavo De Nardin <gustavodn@mandriva.com> 1.6.4-5mdv2007.0
+ Revision: 114259

* Mon May 15 2006 Guillaume Cottenceau <gc@mandrakesoft.com> 1.6.4-4mdk
- rebuild for sparc

* Sat Dec 31 2005 Guillaume Cottenceau <gc@mandrakesoft.com> 1.6.4-3mdk
- Rebuild

* Fri Feb 11 2005 Olivier Blin <oblin@mandrakesoft.com> 1.6.4-2mdk
- security update for CAN-2004-1184, CAN-2004-1185, CAN-2004-1186
  (from Vincent Danen)

