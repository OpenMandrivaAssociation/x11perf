Name:		x11perf
Version:	1.4.1
Release:	%mkrel 4
Summary:	X11 server performance comparison program  
Group:		Development/X11
URL: http://xorg.freedesktop.org
########################################################################
# git clone git://git.mandriva.com/people/pcpa/xorg/app/x11perf xorg/app/x11perf
# cd xorg/app/x11perf
# git-archive --format=tar --prefix=x11perf-1.4.1/ x11perf-1_4_1 | bzip2 -9 > x11perf-1.4.1.tar.bz2
########################################################################
Source:		%{name}-%{version}.tar.bz2
License:	MIT
# Tag x11perf-1.4.1@mandriva at commit 1540dc21e1ef7bb473af7616294e5730e38f66ec
########################################################################
# git format-patch -B -M x11perf-1_4_1..x11perf-1.4.1@mandriva
Patch1: 0001-Bug-10616-Man-page-typo-s-peform-perform.patch
Patch2: 0002-renamed-.cvsignore-.gitignore.patch
Patch3: 0003-Another-man-page-typo-fix-s-aprox.-approx.patch
Patch4: 0004-Bug-9520-Markup-problems-in-Xmark.1x.patch
Patch5: 0005-Rename-.cvsignore-to-.gitignore.patch
Patch6: 0006-Add-Compositing-tests.patch
Patch7: 0007-Fix-typos-in-descriptions-of-compwinwin-1-5-00.patch
Patch8: 0008-Replace-static-ChangeLog-with-dist-hook-to-generate.patch
########################################################################
BuildRoot:	%{_tmppath}/%{name}-root
BuildRequires: x11-util-macros	>= 1.1.5
BuildRequires: libxmu-devel	>= 1.0.4
BuildRequires: libxext-devel	>= 1.0.3
BuildRequires: libxft-devel	>= 2.1.12

%description
The x11perf program runs one or more performance tests and reports how
fast an X server can execute the tests.

%prep

%setup -q -n %{name}-%{version}

%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1

%build
autoreconf -ifs
%configure	--x-includes=%{_includedir}\
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


