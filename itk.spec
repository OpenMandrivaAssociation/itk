%define build_patented	0
%{?_with_patented: %{expand: %%global build_patented 1}}

%define build_review	1
%{?_with_review: %{expand: %%global build_review 1}}

%define build_examples	1
%{?_with_examples: %{expand: %%global build_examples 1}}

%define build_doc	0
%{?_with_doc: %{expand: %%global build_doc 1}}

%define build_java	0
%{?_with_java: %{expand: %%global build_java 1}}

%define build_python	0
%{?_with_python: %{expand: %%global build_python 1}}

%define build_tcl	0
%{?_with_python: %{expand: %%global build_tcl 1}}

%define libname		%mklibname %{name} 4
%define develname	%mklibname %{name} -d
%define short_version	%(echo %{version} | cut -d. -f1,2)

%define itkdir		%{_datadir}/%{name}
%define itklibdir	%{_libdir}/%{name}-%{short_version}
%define itkincludedir	%{_includedir}/%{name}-%{short_version}

Name:		itk
Version:	3.20.0
Release:	5
Epoch:		2
Summary:	Medicine Insight Segmentation and Registration
License:	BSD-like
Group:		Sciences/Other
URL:		http://www.itk.org
Source0:	http://dl.sourceforge.net/sourceforge/itk/InsightToolkit-%{version}.tar.gz
Source1:	http://dl.sourceforge.net/sourceforge/itk/ItkSoftwareGuide-2.4.0.pdf.bz2
Source2:	http://dl.sourceforge.net/sourceforge/itk/DoxygenInsightToolkit-%{version}.tar.gz
BuildRequires:	cmake >= 2.6.0
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xft)
BuildRequires:	pkgconfig(xscrnsaver)
BuildRequires:	pkgconfig(xt)
BuildRequires:	pkgconfig(libpng)
# New tiff is not supported yet
#BuildRequires:	tiff-devel
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(fftw3)
BuildRequires:	graphviz
BuildRequires:	pkgconfig(uuid)
BuildRequires:	tcl-devel

%if %{build_doc}
BuildRequires:	doxygen
# this should signficantly reduce number of pango-WARNING messages
BuildRequires:	urw-fonts
%endif
BuildRequires:	perl
BuildRequires:	pkgconfig(fontconfig)
BuildRequires:	cableswig
%if %{build_java}
BuildRequires:	java-rpmbuild
BuildRequires:	java-devel
BuildRequires:	jpackage-utils
%endif
%if %{build_python}
%py_requires -d
BuildRequires:	python-numarray-devel
Requires:	python-numarray
%endif
%if %{build_tcl}
BuildRequires:	tk-devel >= 8.6
BuildRequires:	tcl-devel >= 8.6
BuildRequires:	tcl
%endif

Patch0:		InsightToolkit-3.20.0-build-install.patch
Patch1:		InsightToolkit-3.20.0-tcl8.6.patch
Patch2:		InsightToolkit-3.20.0-gcc4.6.patch
Patch3:		InsightToolkit-3.20.0-gcc4.7.patch
Patch4:		InsightToolkit-3.20.0-libpng15.patch
Patch5:		InsightToolkit-3.20.0-gzgetc.patch
Patch6:		InsightToolkit-3.20.0-header.patch

%description
ITK is an open-source software system to support the Visible Human Project. 
Currently under active development, ITK employs leading-edge segmentation 
and registration algorithms in two, three, and more dimensions.

The Insight Toolkit was developed by six principal organizations, three 
commercial (Kitware, GE Corporate R&D, and Insightful) and three academic 
(UNC Chapel Hill, University of Utah, and University of Pennsylvania). 
Additional team members include Harvard Brigham & Women's Hospital, 
University of Pittsburgh, and Columbia University. The funding for the 
project is from the National Library of Medicine at the National Institutes 
of Health. NLM in turn was supported by member institutions of NIH (see 
sponsors).

#---------------------------------------------------------------------------------

%package	-n %{libname}
Group:		System/Libraries
Summary:	Medicine Insight Segmentation and Registration
Provides:	%{name} = %{version}-%{release}
Provides:	itk = %{version}-%{release}

%description -n %{libname}
ITK is an open-source software system to support the Visible Human Project.
Currently under active development, ITK employs leading-edge segmentation
and registration algorithms in two, three, and more dimensions.

The Insight Toolkit was developed by six principal organizations, three
commercial (Kitware, GE Corporate R&D, and Insightful) and three academic
(UNC Chapel Hill, University of Utah, and University of Pennsylvania).
Additional team members include Harvard Brigham & Women's Hospital,
University of Pittsburgh, and Columbia University. The funding for the
project is from the National Library of Medicine at the National Institutes
of Health. NLM in turn was supported by member institutions of NIH (see
sponsors).

%files -n %{libname}
%defattr(0644,root,root,0755)
%dir %{itklibdir}
%dir %{itklibdir}/lib*.so.*
%if %{build_java}
%exclude %{itklibdir}/*Java*.so.*
%endif
%if %{build_python}
%exclude %{itklibdir}/*Python*.so.*
%endif
%if %{build_tcl}
%exclude %{itklibdir}/*Tcl*.so.*
%endif
%{_libdir}/InsightToolkit
%{_sysconfdir}/ld.so.conf.d/*

#---------------------------------------------------------------------------------

%package	-n %{develname}
Summary:	ITK header files for building C++ code
Group:		Development/C++
Requires:	%{libname} = %{epoch}:%{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}

%description -n %{develname}
ITK is an open-source software system to support the Visible Human Project. 
Currently under active development, ITK employs leading-edge segmentation 
and registration algorithms in two, three, and more dimensions.

The Insight Toolkit was developed by six principal organizations, three 
commercial (Kitware, GE Corporate R&D, and Insightful) and three academic 
(UNC Chapel Hill, University of Utah, and University of Pennsylvania). 
Additional team members include Harvard Brigham & Women's Hospital, 
University of Pittsburgh, and Columbia University. The funding for the 
project is from the National Library of Medicine at the National Institutes 
of Health. NLM in turn was supported by member institutions of NIH (see 
sponsors). 

%files		-n %{develname}
%defattr(0644,root,root,0755)
%attr(0755,root,root) %{_bindir}/*
%{_includedir}/multiarch*
%dir %{itkincludedir}
%{itkincludedir}/*
%{_includedir}/InsightToolkit
%{itklibdir}/*.cmake
%{itklibdir}/lib*.so
%if %{build_java}
%exclude %{itklibdir}/*Java*.so
%endif
%if %{build_java}
%exclude %{itklibdir}/*Python*.so
%endif
%if %{build_tcl}
%exclude %{itklibdir}/*Tcl*.so
%endif

#---------------------------------------------------------------------------------

%if %{build_examples}

%package	examples
Summary:	C++, Tcl and Python example programs/scripts for ITK
Group:		Development/C++
Requires:	%{libname} = %{EVRD}
BuildArch:	noarch

%description examples
ITK is an open-source software system to support the Visible Human Project. 
Currently under active development, ITK employs leading-edge segmentation 
and registration algorithms in two, three, and more dimensions.

The Insight Toolkit was developed by six principal organizations, three 
commercial (Kitware, GE Corporate R&D, and Insightful) and three academic 
(UNC Chapel Hill, University of Utah, and University of Pennsylvania). 
Additional team members include Harvard Brigham & Women's Hospital, 
University of Pittsburgh, and Columbia University. The funding for the 
project is from the National Library of Medicine at the National Institutes 
of Health. NLM in turn was supported by member institutions of NIH (see 
sponsors). 

%files		examples
%defattr(0644,root,root,0755)
%dir %{itkdir}/examples
%{itkdir}/examples/*
%dir %{itkdir}/data
%{itkdir}/data/*

%endif

#---------------------------------------------------------------------------------

%package	doc
Summary:	Documentation for ITK
Group:		Development/C++
BuildArch:	noarch

%description	doc
ITK is an open-source software system to support the Visible Human Project. 
Currently under active development, ITK employs leading-edge segmentation 
and registration algorithms in two, three, and more dimensions.

The Insight Toolkit was developed by six principal organizations, three 
commercial (Kitware, GE Corporate R&D, and Insightful) and three academic 
(UNC Chapel Hill, University of Utah, and University of Pennsylvania). 
Additional team members include Harvard Brigham & Women's Hospital, 
University of Pittsburgh, and Columbia University. The funding for the 
project is from the National Library of Medicine at the National Institutes 
of Health. NLM in turn was supported by member institutions of NIH (see 
sponsors). 

%files		doc
%defattr(0644,root,root,0755)
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/*

#---------------------------------------------------------------------------------

%if %{build_java}

%package	-n java-%{name}
Summary:	Java bindings for ITK
Group:		Development/Java

%description -n java-%{name}
ITK is an open-source software system to support the Visible Human Project. 
Currently under active development, ITK employs leading-edge segmentation 
and registration algorithms in two, three, and more dimensions.

This package contains Java bindings for ITK.

%files		-n java-%{name}
%defattr(0644,root,root,0755)
%{itklibdir}/java
%{itklibdir}/*Java*.so.*

%package	-n java-%{name}-devel
Summary:	Java development files for ITK bindings
Group:		Development/Other

%description	-n java-%{name}-devel
Java development files for ITK bindings.

%files		-n java-%{name}-devel
%defattr(0644,root,root,0755)
%{itklibdir}/*Java*.so

%endif

#---------------------------------------------------------------------------------

%if %{build_python}

%package	-n python-%{name}
Summary:	Python bindings for ITK
Group:		Development/Python

%description	-n python-%{name}
ITK is an open-source software system to support the Visible Human Project. 
Currently under active development, ITK employs leading-edge segmentation 
and registration algorithms in two, three, and more dimensions.

This package contains Python bindings for ITK.

%files		-n python-%{name}
%defattr(0644,root,root,0755)
%{itklibdir}/*.py
%dir %{itklibdir}/python
%{itklibdir}/python/*
%{itklibdir}/*Python*.so.*
%{python_sitelib}/%{name}

%package	-n python-%{name}-devel
Summary:	Python development files for ITK bindings
Group:		Development/Other

%description	-n python-%{name}-devel
Python development files for ITK bindings.

%files		-n python-%{name}-devel
%defattr(0644,root,root,0755)
%{itklibdir}/*Python*.so

%endif

#---------------------------------------------------------------------------------

%if %{build_tcl}

%package	-n tcl-%{name}
Summary:	Tcl bindings for ITK
Group:		Development/Other

%description	-n tcl-%{name}
ITK is an open-source software system to support the Visible Human Project. 
Currently under active development, ITK employs leading-edge segmentation 
and registration algorithms in two, three, and more dimensions.

This package contains Tcl bindings for ITK.

%files		-n tcl-%{name}
%defattr(0644,root,root,0755)
%{_bindir}/itkwish*
%dir %{itklibdir}/tcl
%{itklibdir}/tcl/*
%{itklibdir}/*Tcl*.so.*
%{tcl_sitearch}/InsightToolkit

%package	-n tcl-%{name}-devel
Summary:	Tcl development files for ITK bindings
Group:		Development/Other

%description	-n tcl-%{name}-devel
Tcl development files for ITK bindings.

%files		-n tcl-%{name}-devel
%defattr(0644,root,root,0755)
%{itklibdir}/*Tcl*.so

%endif


#---------------------------------------------------------------------------------

%prep
%setup -q -n InsightToolkit-%{version}

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

# doc
bunzip2 %{SOURCE1} -c > ItkSoftwareGuide.pdf

# remove CVS dirs, if exists
find -name CVS -type d | xargs rm -rf


%build
%cmake \
	-DINSTALL_WRAP_ITK_COMPATIBILITY=OFF \
	-DITK_INSTALL_LIB_DIR=/%{_lib}/%{name}-%{short_version} \
	-DITK_INSTALL_DATA_DIR=/share/%{name} \
	-DITK_INSTALL_INCLUDE_DIR=/include/%{name}-%{short_version} \
	-DITK_DATA_ROOT:PATH=%{itkdir} \
%if %{build_review}
	-DITK_USE_REVIEW:BOOL=ON \
	-DITK_USE_CONSOLIDATED_MORPHOLOGY:BOOL=ON \
%else
	-DITK_USE_REVIEW:BOOL=OFF \
%endif
	-DUSE_FFTWF:BOOL=ON \
	-DUSE_FFTWD:BOOL=ON \
	-DFFTW_INCLUDE_PATH:PATH=%{_includedir} \
	-DBUILD_SHARED_LIBS=ON \
%if %{build_java}
	-DJAVA_INCLUDE_PATH=%{java_home}/include \
	-DJAVA_INCLUDE_PATH2=%{java_home}/include/linux \
	-DJAVA_AWT_INCLUDE_PATH=%{java_home}/include \
	-DJAVA_AWT_LIBRARY=%{java_home}/jre/lib/i386/libawt.so \
	-DITK_CSWIG_JAVA=ON \
%else
	-DITK_CSWIG_JAVA=OFF \
%endif
%if %{build_python}
	-DITK_CSWIG_PYTHON=ON \
	-DWRAP_ITK_PYTHON=ON \
	-DITK_USE_PYTHON_NUMARRAY=ON \
%else
	-DITK_CSWIG_PYTHON=OFF \
	-DWRAP_ITK_PYTHON=OFF \
%endif
%if %{build_tcl}
	-DITK_CSWIG_TCL=ON \
	-DWRAP_ITK_TCL=ON \
%else
	-DITK_CSWIG_TCL=OFF \
	-DWRAP_ITK_TCL=OFF \
%endif
%if %{build_doc}
	-DBUILD_DOXYGEN:BOOL=ON \
%else
	-DBUILD_DOXYGEN:BOOL=OFF \
%endif
%if %{build_examples}
	-DBUILD_EXAMPLES=ON \
%else
	-DBUILD_EXAMPLES=OFF \
%endif
%if %{build_patented}
	-DITK_USE_PATENTED=ON \
%else
	-DITK_USE_PATENTED=OFF \
%endif
	-DITK_USE_SYSTEM_TIFF=OFF \
	-DITK_USE_SYSTEM_PNG=ON \
	-DITK_USE_SYSTEM_ZLIB=ON

%make

# build docs
%if %{build_doc}
    doxygen Utilities/Doxygen/doxygen.config
%endif

%install
rm -rf %{buildroot}

%makeinstall_std -C build

# install ld.so.conf path
install -d -m 755 %buildroot/%{_sysconfdir}/ld.so.conf.d
cat > %{buildroot}/%{_sysconfdir}/ld.so.conf.d/%{_lib}%{name}.conf <<_EOF
%{itklibdir}
_EOF

# install docs
install -d -m 755 %{buildroot}/%{_docdir}/%{name}
%if %{build_doc}
    cp -a build/Utilities/Doxygen/html %{buildroot}/%{_docdir}/%{name}/api
    cp -fa	Documentation/InsightDeveloperStart.pdf			\
		Documentation/Style.pdf					\
		ItkSoftwareGuide.pdf					\
	%{buildroot}/%{_docdir}/%{name}
    cp -fa README.html Documentation/DeveloperList.txt Copyright	\
	%{buildroot}/%{_docdir}/%{name}
%else
    tar zxf %{SOURCE2} -C %{buildroot}%{_docdir}/%{name}
    mv %{buildroot}%{_docdir}/%{name}/{DoxygenInsightToolkit-%{version}/,}html
    rm -fr %{buildroot}%{_docdir}/%{name}/DoxygenInsightToolkit-%{version}
    cp -fa Documentation/{README.html,InsightDeveloperStart.pdf,Style.pdf} \
	ItkSoftwareGuide.pdf Copyright %{buildroot}%{_docdir}/%{name}
%endif

%if %{build_examples}
    # install examples
    install -d -m 755 %{buildroot}/%{itkdir}/examples
    cp -a Testing %{buildroot}/%{itkdir}/examples
    cp -a Examples %{buildroot}/%{itkdir}/examples

    # get rid of unwanted files
    pushd %{buildroot}%{itkdir}
    find . -name "*.o" -o -name "CMake*" -o -name "cmake.*"		\
	-o -name .NoDartCoverage -o -name .NoDartCoverage		\
	-o -name Makefile -o -name DartTestfile.txt			\
	-exec rm {} \;
    popd

    #install data
    mv %{buildroot}/%{itkdir}/examples/Testing/Data %{buildroot}/%{itkdir}/data
%endif

# multiarch support
%multiarch_includes  %{buildroot}/%{itkincludedir}/Utilities/itksys/FundamentalType.h

# add some links for the default target directories
ln -sf %{itklibdir} %{buildroot}%{_libdir}/InsightToolkit
ln -sf %{itkincludedir} %{buildroot}%{_includedir}/InsightToolkit

%if %{build_python}
   mkdir -p %{buildroot}%{python_sitelib}
   ln -sf %{itklibdir}/python %{buildroot}%{python_sitelib}/%{name}
%endif

%if %{build_tcl}
    mkdir -p %{buildroot}%{_bindir}
    mkdir -p %{buildroot}%{tcl_sitearch}
    ln -sf %{itklibdir}/tcl %{buildroot}%{tcl_sitearch}/InsightToolkit
    mv -f %{buildroot}/%{itklibdir}/itkwish-*  %{buildroot}/%{_bindir}
    ln -sf itkwish %{buildroot}/%{_bindir}/itkwish*
    rm -f %{buildroot}/%{itklibdir}/itkwish
%endif

%check

cd build
# set the lib path needed to run the tests
export LD_LIBRARY_PATH=`pwd`/bin
# ctest

%changelog
* Mon Jul 09 2012 Anton Chernyshov <ach@rosalab.ru> 3.20.0-1
- Fix BuildRequires
- Add patch to build with gcc-4.6

* Sat Feb 05 2011 Funda Wang <fwang@mandriva.org> 2:3.20.0-3mdv2011.0
+ Revision: 636015
- tighten BR

* Thu Sep 02 2010 Thierry Vignaud <tv@mandriva.org> 2:3.20.0-2mdv2011.0
+ Revision: 575206
- let the doc subpackage be noarch

* Wed Jul 14 2010 Paulo Andrade <pcpa@mandriva.com.br> 2:3.20.0-1mdv2011.0
+ Revision: 553420
- Update to version 3.20.0.

* Thu May 27 2010 Paulo Andrade <pcpa@mandriva.com.br> 2:3.16.0-4mdv2010.1
+ Revision: 546357
- Correct 2010.0 upgrade conflict
- Generate itk-doc from prebuilt files if documentation build is disabled

* Thu May 13 2010 Paulo Andrade <pcpa@mandriva.com.br> 2:3.16.0-3mdv2010.1
+ Revision: 544710
- Make itk-examples package instalable

* Tue May 11 2010 Frederic Crozat <fcrozat@mandriva.com> 2:3.16.0-2mdv2010.1
+ Revision: 544488
- force rebuild
- force rebuild

  + Paulo Andrade <pcpa@mandriva.com.br>
    - Disable documentation build
    - Add epoch to requires of devel
    - Add libuuid-devel to build requires
    - Create a symbolic link to tcldir, so that itkwish works "out of the box",
      without requiring extra setup to specify where InsightToolkit tcl interface
      is located.
    - Correct leftover of manual builds before setting ITK_INSTALL_LIB_DIR.
      Correct generation of symbolic link to %%{python_sitelib}.
    - o Update to latest upstream release itk 3.12.0.
      o Enable Python and Tcl wrapping by default.
      o Use same pattern as vtk package for libdir and includedir,
      that is to use the "reduced" name itk-major.minor instead of InsightToolkit
      o Add extra -devel packages for .so files.

  + Funda Wang <fwang@mandriva.org>
    - New version 3.16.0

  + Gaëtan Lehmann <glehmann@mandriva.org>
    - Some tests are broken - don't run the tests for now
    - 3.14
    - disable python and tcl - they'll be built in wrapitk package
    - build review and consolidated morphology - they are required to build wrapitk
    - patch for unversioned slatec lib (from upstream)

  + Helio Chissini de Castro <helio@mandriva.com>
    - Updates for current version
    - Added flags for build doc, and python and java bindings and examples.
      Doc are disabled due the huge amount of time to compile. Will be replaced with upstream ready doc.
      Java and python bindings are disabled due a gcc 4.x compilation issues ( TODO )
    - Removed data package, since is used only to examples package
    - Added %%_lib in ld.so.conf.d conf to allow biarch installs
    - Fixed library soname
    - Added patch to install 64 libs in proper place

  + Emmanuel Andry <eandry@mandriva.org>
    - New version
    - use major

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Adam Williamson <awilliamson@mandriva.org>
    - rebuild for new era
    - spec clean
    - update file lists
    - drop headertest.patch (merged upstream)
    - drop the various external sources that were rolled into upstream
    - new license policy
    - drop unneeded vars
    - new release 3.4.0

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - buildrequires X11-devel instead of XFree86-devel


* Thu Aug 31 2006 Gaëtan Lehmann (INRA) <glehmann@mandriva.org> 
+ 2006-08-31 17:38:23 (59090)
use RPM_OPT_FLAGS

* Tue Aug 29 2006 Gaëtan Lehmann (INRA) <glehmann@mandriva.org> 
+ 2006-08-29 11:54:15 (58628)
rebuild (again) to sync i586 and x86_64 packages

* Mon Jul 31 2006 Gaëtan Lehmann (INRA) <glehmann@mandriva.org> 
+ 2006-07-31 21:36:23 (42881)
rebuild

* Sun Jul 30 2006 Gaëtan Lehmann (INRA) <glehmann@mandriva.org> 
+ 2006-07-30 09:54:36 (42650)
Import itk

* Tue Jul 18 2006 Gaetan Lehmann <gaetan.lehmann@jouy.inra.fr> 2.8.1-1mdv2007.0
- 2.8.1
- drop patch 1 (merged upstream)
- update patch 11
- replace patches 8, 9 and 10 by patch 10
- no more requires cableswig (wrapping is done in wrapitk)
- update source 4 (enhanced erode and dilate filters)

* Wed Apr 12 2006 Gaetan Lehmann <gaetan.lehmann@jouy.inra.fr> 2.6.0-6-mdk
- fix post install problem

* Mon Apr 10 2006 Gaetan Lehmann <glehmann@n4.mandriva.com> 2.6.0-5mdk
- update source 4 (enhanced erode and dilate filters)
- run tests

* Fri Apr 07 2006 Gaetan Lehmann <gaetan.lehmann@jouy.inra.fr> 2.6.0-4mdk
- Patch1: fix itk::VectorImage invalid oveloaded methods
- drop tcl support (will be supproted by wrapitk)
- add ImageCompare in devel package

* Mon Mar 27 2006 Gaetan Lehmann <gaetan.lehmann@jouy.inra.fr> 2.6.0-3mdk
- update reconstruction filters
- fix itkwish attr

* Tue Mar 21 2006 Gaetan Lehmann <gaetan.lehmann@jouy.inra.fr> 2.6.0-2mdk
- fix missing itkwish

* Tue Mar 14 2006 Gaetan Lehmann <gaetan.lehmann@jouy.inra.fr> 2.6.0-1mdk
- 2.6.0
- remove patches 1 to 7: merged or fixed upstream
- update histogram based dilation/erosion filters
- patch 30: fix test build with new reconstruction filters

* Tue Mar 07 2006 Gaetan Lehmann <gaetan.lehmann@jouy.inra.fr> 2.4.1-5mdk
- add several patch to enhance perf and fix bugs
- drop python support (will by provided by wrapitk)
- add optional patches from wrapitk
- force /usr/bin/c++ compiler

* Fri Jan 20 2006 Oden Eriksson <oeriksson@mandriva.com> 2.4.1-4mdk
- fix deps

* Sat Jan 07 2006 Oden Eriksson <oeriksson@mandriva.com> 2.4.1-3mdk
- rebuilt against soname aware deps (tcl/tk)
- fix deps

* Sun Dec 11 2005 Gaetan Lehmann <gaetan.lehmann@jouy.inra.fr> 2.4.1-2mdk
- multiarch support

* Fri Dec 09 2005 Gaetan Lehmann <gaetan.lehmann@jouy.inra.fr> 2.4.1-1mdk
- new release 2.4.1
- use Release build
- fix lib path in cmake files on x86_64
- pre-requires lib package for wrappers. ldconfig need to know where are
  the files

* Sat Dec 03 2005 Gaetan Lehmann <gaetan.lehmann@jouy.inra.fr> 2.4.0-1mdk
- new release 2.4.0

* Thu Mar 24 2005 Gaetan Lehmann <gaetan.lehmann@jouy.inra.fr> 2.0.1-1mdk
- New release 2.0.1
- Use mkrel
- add "--with patented" switch
- fix wrong tcl group

* Wed Mar 02 2005 Gaetan Lehmann <gaetan.lehmann@jouy.inra.fr> 2.0.0-2mdk
- add morpho filters in wrappers (patch1)
- fix some lint

* Sun Feb 13 2005 Gaetan Lehmann <gaetan.lehmann@jouy.inra.fr> 2.0.0-1mdk
- 2.0.0
- add wrappers

* Mon Jan 31 2005 Gaetan Lehmann <gaetan.lehmann@jouy.inra.fr> 1.10.0-0.cvs20050131.1mdk
- 1.10.0 cvs
- build still fail with wrapper so no wrapper avaible :-(
- add doc and devel packages
- use libitk name
- initial contrib release

* Mon Sep 27 2004 Fabrice Bellet <Fabrice.Bellet@creatis.insa-lyon.fr> 1.8.1-2
- add an example packages.

* Wed Sep 22 2004 Fabrice Bellet <Fabrice.Bellet@creatis.insa-lyon.fr> 1.8.1-1
- update to version 1.8.1.

* Thu Sep 09 2004 Fabrice Bellet <Fabrice.Bellet@creatis.insa-lyon.fr> 1.8.0-2
- fix CC and CXX to be consistent with the VTK package.

* Wed Sep 08 2004 Fabrice Bellet <Fabrice.Bellet@creatis.insa-lyon.fr> 1.8.0-1
- update to version 1.8.0.

* Thu May 27 2004 Fabrice Bellet <Fabrice.Bellet@creatis.insa-lyon.fr> 1.6.0-3
- rebuild for Fedora Core 2
- debuginfo rebuild

* Mon Feb 23 2004 Fabrice Bellet <Fabrice.Bellet@creatis.insa-lyon.fr> 1.6.0-2
- update to version 1.6.0.

* Wed Oct 29 2003 Fabrice Bellet <Fabrice.Bellet@creatis.insa-lyon.fr>
- initial release 1.4.0.

