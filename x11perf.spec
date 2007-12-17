Name:		x11perf
Version:	1.4.1
Release:	%mkrel 3
Summary:	X11 server performance comparison program  
Group:		Development/X11
Source:		http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License:	MIT

BuildRequires:	libx11-devel >= 1.0.0
BuildRequires:	libxmu-devel >= 1.0.0
BuildRequires:	x11-util-macros >= 1.0.1

%description
The x11perf program runs one or more performance tests and reports how
fast an X server can execute the tests.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/X11/x11perfcomp
%{_mandir}/man1/*


