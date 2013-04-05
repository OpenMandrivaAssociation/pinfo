Summary: 	Przemek's Info Viewer - a (much) better info
Name: 		pinfo
Version: 	0.6.9
Release: 	14
Group: 		Development/Other
BuildRequires: 	ncurses-devel
BuildRequires:  texinfo
License: 	GPL
Url: 		http://alioth.debian.org/project/showfiles.php?group_id=30592
Source0: 	http://alioth.debian.org/download.php/1498/%{name}-%{version}.tar.bz2
Patch0:		pinfo-0.6.9-lzma-support.patch
Patch1:		pinfo-0.6.9-as-needed.patch

%description
Hypertext info file viewer. User interface similar to lynx.
It is based on ncurses. It can handle now as well info
pages as man pages. Regexp searching included.

%prep
%setup -q
%patch0 -p1 -b .lzma_support
%patch1 -p1

%build
#needed by patch 1
aclocal
libtoolize --copy --force
autoreconf
%configure 
%make
%make -C po

%install
%makeinstall_std

%find_lang %{name}

ln -s pinfo %{buildroot}%{_bindir}/pman

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog README TECHSTUFF
%config(noreplace) %{_sysconfdir}/pinforc
%{_bindir}/*
%{_mandir}/*/*
%{_infodir}/*


%changelog
* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 0.6.9-10mdv2011.0
+ Revision: 667775
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.6.9-9mdv2011.0
+ Revision: 607176
- rebuild

* Mon Mar 15 2010 Oden Eriksson <oeriksson@mandriva.com> 0.6.9-8mdv2010.1
+ Revision: 520199
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.6.9-7mdv2010.0
+ Revision: 426690
- rebuild

* Thu Dec 25 2008 Oden Eriksson <oeriksson@mandriva.com> 0.6.9-6mdv2009.1
+ Revision: 319063
- rebuild

* Mon Aug 18 2008 Emmanuel Andry <eandry@mandriva.org> 0.6.9-5mdv2009.0
+ Revision: 273276
- fix build with p1 from gentoo
- p1 needs autotools to be executed

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 0.6.9-4mdv2008.1
+ Revision: 179237
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - fix no-buildroot-tag

* Mon Sep 24 2007 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.6.9-3mdv2008.0
+ Revision: 92671
- spec cosmetics
- add lzma support (fixes #33913)

* Wed Aug 29 2007 Oden Eriksson <oeriksson@mandriva.com> 0.6.9-2mdv2008.0
+ Revision: 74316
- Import pinfo




* Mon Sep 18 2006 Gwenole Beauchesne <gbeauchesne@mandriva.com> 0.6.9-2mdv2007.0
- Rebuild

* Thu Apr 20 2006 Thierry Vignaud <tvignaud@mandriva.com> 0.6.9-1mdk
- new release
- new URL
- remove patch 0 (merged upstream)
- use %%mkrel
- cleanup

* Sun Jan 01 2006 Mandriva Linux Team <http://www.mandrivaexpert.com/> 0.6.8-2mdk
- Rebuild

* Wed Aug 27 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.6.8-1mdk
- new release
- fix url

* Sun Jun 15 2003 Stefan van der Eijk <stefan@eijk.nu> 0.6.7-2mdk
- BuildRequires

* Thu Feb 13 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.6.7-1mdk
- new release

* Thu Jan 02 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.6.6p1-2mdk
- add missing info doc and locales

* Thu Jul 25 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.6.6p1-1mdk
- new release
- gcc3.2 rebuild

* Sun May 19 2002 Yves Duret <yduret@mandrakesoft.com> 0.6.5p3-1mdk
- version 0.6.5p3.

* Tue Apr 23 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.6.5p2-2mdk
- s/SAFE-GROUP=nobody/SAFE-GROUP=nogroup/ in etc/pinforc [Patch1]
  (saw by Ural Khassanov)

* Thu Apr 04 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.6.5p2-1mdk
- new release

* Thu Dec 06 2001 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.6.4-1mdk
- new release

* Sun Aug 05 2001 Yves Duret <yduret@mandrakesoft.com> 0.6.3-2mdk
- use symlinks instead of hard link !

* Fri Jul 20 2001 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.6.3-1mdk
- new release

* Mon Jul 16 2001 Yves Duret <yduret@mandrakesoft.com> 0.6.2-1mdk
- version 0.6.2
- heavy spec clean up

* Tue May  8 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 0.6.1-1mdk
- version 0.6.1

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 0.6.0-2mdk
- automatically added BuildRequires

* Fri Jul 21 2000 Francis Galiegue <fg@mandrakesoft.com> 0.6.0-1mdk
- 0.6.0
- BMacros

* Thu Mar 16 2000 Francis Galiegue <francis@mandrakesoft.com> 0.5.9-2mdk
- Spec file changes
- Changed group to match 7.1 specs
- now there's pman, too
- Let spec-helper do its job

* Fri Feb 18 2000 Francis Galiegue <francis@mandrakesoft.com> 0.5.9-1mdk
- First Mandrake RPM
