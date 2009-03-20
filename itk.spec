%define build_patented	0
%{?_with_patented: %{expand: %%global build_patented 1}}

%define build_review	0
%{?_with_review: %{expand: %%global build_review 1}}

%define build_examples	1
%{?_with_examples: %{expand: %%global build_examples 1}}

%define build_doc	1
%{?_with_doc: %{expand: %%global build_doc 1}}

%define build_java	0
%{?_with_java: %{expand: %%global build_java 1}}

%define build_python	1
%{?_with_python: %{expand: %%global build_python 1}}

%define build_tcl	1
%{?_with_python: %{expand: %%global build_tcl 1}}

%define name		itk
%define version		3.12.0
%define libname		%mklibname %{name} 3
%define develname	%mklibname %{name} -d
%define short_version	%(echo %{version} | cut -d. -f1,2)

%define itkdir		%{_datadir}/%{name}
%define itklibdir	%{_libdir}/%{name}-%{short_version}
%define itkincludedir	%{_includedir}/%{name}-%{short_version}

Name:		%{name}
Version:	%{version}
Release:	%mkrel 1
Summary:	Medicine Insight Segmentation and Registration
License:	BSD-like
Group:		Sciences/Other
URL:		http://www.itk.org
Source0:	http://dl.sourceforge.net/sourceforge/itk/InsightToolkit-%{version}.tar.gz
Source1:	http://dl.sourceforge.net/sourceforge/itk/ItkSoftwareGuide-2.4.0.pdf.bz2
BuildRequires:	cmake >= 2.6.0
BuildRequires:	X11-devel
BuildRequires:	png-devel
BuildRequires:	tiff-devel
BuildRequires:	zlib-devel
BuildRequires:	fftw3-devel
BuildRequires:	graphviz
%if %{build_doc}
BuildRequires:	doxygen
%endif
BuildRequires:	perl
BuildRequires:	fontconfig
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
%endif
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

Patch0:		InsightToolkit-3.10.0-build-install.patch
Patch1:		itk-3.12.0-tcl8.6.patch
Patch2:		itk-3.12.0-tk8.6.patch

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
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}
Provides:	lib%{name}-devel = %{version}

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
Requires:	%{libname} = %{version}
Obsoletes:	%{name}-data

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

%if %{build_doc}

%package	doc
Summary:	Documentation for ITK
Group:		Development/C++

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

%endif

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
%{itklibdir}/*.py
%dir %{itklibdir}/tcl
%{itklibdir}/tcl/*
%{itklibdir}/*Tcl*.so.*

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

%patch0 -p0 -b build_install
%patch1 -p1
%patch2 -p1

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
	-DITK_USE_SYSTEM_TIFF=ON \
	-DITK_USE_SYSTEM_PNG=ON \
	-DITK_USE_SYSTEM_ZLIB=ON

make

# build docs
%if %{build_doc}
    cd build
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
%if %{build_doc}
    install -d -m 755 %{buildroot}/%{_docdir}/%{name}
    cp -a build/Utilities/Doxygen/html %{buildroot}/%{_docdir}/%{name}/api
    cp -fa	Documentation/InsightDeveloperStart.pdf			\
		Documentation/Style.pdf					\
		ItkSoftwareGuide.pdf					\
	%{buildroot}/%{_docdir}/%{name}
    cp -fa README.html Documentation/DeveloperList.txt Copyright	\
	%{buildroot}/%{_docdir}/%{name}
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

# only cmake files there...
mv -f %{buildroot}%{_libdir}/InsightToolkit/*.cmake %{buildroot}%{itklibdir}
rmdir %{buildroot}%{_libdir}/InsightToolkit

# add some links for the default target directories
ln -sf %{itklibdir} %{buildroot}%{_libdir}/InsightToolkit
ln -sf %{itkincludedir} %{buildroot}%{_includedir}/InsightToolkit

%if %{build_python}
   ln -sf %{itklibdir}/python %{buildroot}%{python_sitelib}/%{name}
%endif

%if %{build_tcl}
    mv -f %{buildroot}%{itklibdir}/itkwish* %{buildroot}%{_bindir}
%endif

%clean
rm -rf %{buildroot}
