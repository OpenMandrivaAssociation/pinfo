Summary: 	Przemek's Info Viewer - a (much) better info
Name: 		pinfo
Version: 	0.6.9
Release: 	%mkrel 5
Group: 		Development/Other
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: 	ncurses-devel
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
rm -rf %{buildroot}

%makeinstall_std

%find_lang %{name}

ln -s pinfo %{buildroot}%{_bindir}/pman

%post
%_install_info %{name}.info

%preun
%_remove_install_info %{name}.info

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog README TECHSTUFF
%config(noreplace) %{_sysconfdir}/pinforc
%{_bindir}/*
%{_mandir}/*/*
%{_infodir}/*
