Name:		x11perf
Version:	1.5.4
Release:	4
Summary:	X11 server performance comparison program
Group:		Development/X11
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License:       MIT
 
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
%configure2_5x

%make

%install
%makeinstall_std

%files
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/X11/x11perfcomp
%{_mandir}/man1/*




%changelog
* Sat Sep 10 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 1.5.4-1mdv2012.0
+ Revision: 699275
- update to new version 1.5.4

* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.5.3-2
+ Revision: 671239
- mass rebuild

* Thu Jan 06 2011 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.5.3-1mdv2011.0
+ Revision: 629001
- New version: 1.5.3
- Use configure2_5x
- Fix spec file indentation and white spaces
- Don't pass redundant configure variables

* Wed Sep 22 2010 Thierry Vignaud <tv@mandriva.org> 1.5.2-1mdv2011.0
+ Revision: 580458
- new release

* Wed Nov 11 2009 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.5.1-1mdv2010.1
+ Revision: 464648
- New version: 1.5.1

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.5-3mdv2009.1
+ Revision: 351255
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.5-2mdv2009.0
+ Revision: 226009
- rebuild
- BuildRequires libxft-devel
- BuildRequires libxrender-devel
- new release

* Tue Feb 12 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.4.1-5mdv2008.1
+ Revision: 166445
- evert to use upstream tarball, build requires and remove non mandatory local patches.

* Tue Jan 22 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.4.1-4mdv2008.1
+ Revision: 156424
- Add extra commits to package, including composite tests.

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Aug 30 2007 Adam Williamson <awilliamson@mandriva.org> 1.4.1-3mdv2008.0
+ Revision: 76331
- rebuild for 2008
- simplify file list, own %%_libdir/X11/x11perfcomp
- add description
- spec clean


* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Thu May 25 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-25 20:17:57 (31598)
- X11R7.1

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository

