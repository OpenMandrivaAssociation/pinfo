Summary: 	Przemek's Info Viewer - a (much) better info
Name: 		pinfo
Version: 	0.6.10
Release: 	1
Group: 		Development/Other
BuildRequires: 	ncurses-devel gettext-devel autoconf automake
License: 	GPL
Url: 		http://alioth.debian.org/project/showfiles.php?group_id=30592
Source0: 	http://alioth.debian.org/download.php/1498/%{name}-%{version}.tar.bz2
Patch:		pinfo-0.6.10-lzma-xz-lzip.patch
Patch1:		pinfo-0.6.9-as-needed.patch

%description
Hypertext info file viewer. User interface similar to lynx.
It is based on ncurses. It can handle now as well info
pages as man pages. Regexp searching included.

%prep
%setup -q
%patch -p1 -b .lzmaXzLzip~
%patch1 -p1 -b .as_needed~
./autogen.sh --no-configure

%build
%configure 
%make
%make -C po

%install
rm -rf %{buildroot}

%makeinstall_std

%find_lang %{name}

ln -s pinfo %{buildroot}%{_bindir}/pman

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog README TECHSTUFF
%config(noreplace) %{_sysconfdir}/pinforc
%{_bindir}/*
%{_mandir}/*/*
%{_infodir}/*
