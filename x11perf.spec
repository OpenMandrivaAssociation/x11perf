Name:		x11perf
Version:	1.6.0
Release:	5
Summary:	X11 server performance comparison program
Group:		Development/X11
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License:	MIT
 
BuildRequires: pkgconfig(x11) >= 1.0.0
BuildRequires: pkgconfig(xmu) >= 1.0.0
BuildRequires: pkgconfig(xft)
BuildRequires: x11-util-macros >= 1.0.1

%description
The x11perf program runs one or more performance tests and reports how
fast an X server can execute the tests.

%prep
%setup -q -n %{name}-%{version}

%build
autoreconf -fi
%configure

%make

%install
%makeinstall_std

%files
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/X11/x11perfcomp
%{_mandir}/man1/*
