Summary: 	Przemek's Info Viewer - a (much) better info
Name: 		pinfo
Version: 	0.6.9
Release: 	%mkrel 2
Group: 		Development/Other
BuildRequires: 	ncurses-devel
License: 	GPL
Url: 		http://alioth.debian.org/project/showfiles.php?group_id=30592
Source: 	http://alioth.debian.org/download.php/1498/%name-%version.tar.bz2
BuildRoot: 	%_tmppath/%name-%version-%release-root

%description
Hypertext info file viewer. User interface similar to lynx.
It is based on ncurses. It can handle now as well info
pages as man pages. Regexp searching included.

%prep
%setup -q

%build
%configure 
%make

make -C po install

%install
mkdir -p $RPM_BUILD_ROOT/{%_sysconfdir,%_bindir,%_mandir/man1}
make install DESTDIR=$RPM_BUILD_ROOT

%find_lang %name

cd $RPM_BUILD_ROOT/%_bindir
ln -fs pinfo pman

%files -f %name.lang
%defattr(-,root,root)
%doc ABOUT-NLS AUTHORS COPYING ChangeLog INSTALL NEWS README TECHSTUFF
%config(noreplace) %_sysconfdir/pinforc
%_bindir/*
%_mandir/*/*
%_infodir/*

%clean
rm -rf $RPM_BUILD_ROOT

%preun
%_remove_install_info %name.info

%post
%_install_info %name.info

true
