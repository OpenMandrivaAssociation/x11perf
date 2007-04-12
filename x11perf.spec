Name: x11perf
Version: 1.4.1
Release: %mkrel 2
Summary: X11 server performance comparison program  
Group: Development/X11
Source: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: libxmu-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

%description
CHECK

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
%{_bindir}/x11perfcomp
%{_bindir}/x11perf
%{_libdir}/X11/x11perfcomp/Xmark
%{_libdir}/X11/x11perfcomp/perfratio
%{_libdir}/X11/x11perfcomp/fillblnk
%{_libdir}/X11/x11perfcomp/perfboth
%{_mandir}/man1/x11perf.1x.bz2
%{_mandir}/man1/x11perfcomp.1x.bz2
%{_mandir}/man1/Xmark.1x.bz2


