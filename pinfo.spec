Summary:	Przemek's Info Viewer - a (much) better info
Name:		pinfo
Version:	0.6.10
Release:	3
Group:		Development/Other
License:	GPLv2
Url:		http://alioth.debian.org/project/showfiles.php?group_id=30592
Source0:	http://alioth.debian.org/download.php/1498/%{name}-%{version}.tar.bz2
Patch0:		pinfo-0.6.10-lzma-xz-lzip.patch
Patch1:		pinfo-0.6.9-as-needed.patch
BuildRequires:	autoconf
BuildRequires:	texinfo
BuildRequires:	gettext-devel
BuildRequires:	pkgconfig(ncurses)

%description
Hypertext info file viewer. User interface similar to lynx.
It is based on ncurses. It can handle now as well info
pages as man pages. Regexp searching included.

%prep
%setup -q
%apply_patches
./autogen.sh --no-configure

%build
%configure 
%make
%make -C po

%install
%makeinstall_std

%find_lang %{name}

ln -s pinfo %{buildroot}%{_bindir}/pman

%files -f %{name}.lang
%doc AUTHORS ChangeLog README TECHSTUFF
%config(noreplace) %{_sysconfdir}/pinforc
%{_bindir}/*
%{_mandir}/*/*
%{_infodir}/*

