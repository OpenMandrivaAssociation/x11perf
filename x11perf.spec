Name:		x11perf
Version:	1.7.0
Release:	1
Summary:	X11 server performance comparison program
Group:		Development/X11
URL:		https://xorg.freedesktop.org
Source0:	https://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.xz
License:	MIT
 
BuildRequires:	pkgconfig(x11) >= 1.0.0
BuildRequires:	pkgconfig(xmu) >= 1.0.0
BuildRequires:	pkgconfig(xft)
BuildRequires:	pkgconfig(xorg-macros)

%description
The x11perf program runs one or more performance tests and reports how
fast an X server can execute the tests.

%prep
%autosetup -p1

%build
autoreconf -fi
%configure
%make_build

%install
%make_install

%files
%{_bindir}/*
%{_datadir}/X11/x11perfcomp/
%doc %{_mandir}/man1/*
