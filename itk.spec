%define build_java 0
%{?_with_java: %{expand: %%global build_java 1}}

%define build_patented 0
%{?_with_patented: %{expand: %%global build_patented 1}}

%define name	itk
%define version 3.8.0
%define release 1

%define	major		0
%define libname		%mklibname %{name} %{major}
%define develname	%mklibname %{name} -d

Summary:	Medicine Insight Segmentation and Registration
Name:		%{name}
Version:	%{version}
Release:	%mkrel %{release}
License:	BSD-like
Group:		Sciences/Other
URL:		http://www.itk.org
Source0:	http://ovh.dl.sourceforge.net/sourceforge/itk/InsightToolkit-%{version}.tar.gz
Source1:	http://ovh.dl.sourceforge.net/sourceforge/itk/ItkSoftwareGuide-2.4.0.pdf.bz2
Patch10:	wrapping-convenience-patches.patch
#Patch11:	python-interface-patches.patch
BuildRequires:	cmake >= 1.8.3
BuildRequires:  X11-devel
BuildRequires:  png-devel
BuildRequires:  tiff-devel
BuildRequires:  zlib-devel
BuildRequires:  gcc-c++
BuildRequires:	fftw3-devel
BuildRequires:	graphviz
BuildRequires:  doxygen
BuildRequires:  perl
BuildRequires:	fontconfig
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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

%package -n %{libname}
Group:          System/Libraries
Summary:        Medicine Insight Segmentation and Registration
Provides:	%{name} = %{version}-%{release}
Provides:	InsightToolkit = %{version}-%{release}

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

%package  -n %{develname}
Summary:	ITK header files for building C++ code
Group:		Development/C++
Requires:	gcc-c++ 
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

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

%package examples
Summary:	C++, Tcl and Python example programs/scripts for ITK
Group:		Development/C++
Requires:	%{name}-data = %{version}
Requires:       %{libname} = %{version}

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

%package data
Summary:	These data are required to run various examples from the examples package
Group:		Development/C++

%description data
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

%package doc
Summary:	Documentation for ITK
Group:		Development/C++

%description doc
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

# %package -n python-%{name}
# Summary:	Python bindings for ITK
# Group:		Development/Python
# Requires:	python
# Requires:	python-numarray
# Requires:	%{name} = %{version}
# Requires(pre):	%{name} = %{version}
# Obsoletes:	%{name}-pyhon
# Provides:	%{name}-pyhon
# 
# %description -n python-%{name}
# ITK is an open-source software system to support the Visible Human Project. 
# Currently under active development, ITK employs leading-edge segmentation 
# and registration algorithms in two, three, and more dimensions.
# 
# The Insight Toolkit was developed by six principal organizations, three 
# commercial (Kitware, GE Corporate R&D, and Insightful) and three academic 
# (UNC Chapel Hill, University of Utah, and University of Pennsylvania). 
# Additional team members include Harvard Brigham & Women's Hospital, 
# University of Pittsburgh, and Columbia University. The funding for the 
# project is from the National Library of Medicine at the National Institutes 
# of Health. NLM in turn was supported by member institutions of NIH (see 
# sponsors). 

%if %build_java
%package -n java-%{name}
Summary: Java bindings for ITK
Group: Development/Java
Requires: %{name} = %{version}
Requires(pre):	%{name} = %{version}
Obsoletes:      %{name}-java
Provides:       %{name}-java

%description -n java-%{name}
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
%endif

# %package -n tcl-%{name}
# Summary: TCL bindings for ITK
# Group: Development/Other
# Requires:	%{name} = %{version}
# Requires(pre):	%{name} = %{version}
# Requires:	tcl
# Obsoletes:      %{name}-tcl
# Provides:       %{name}-tcl
# 
# %description -n tcl-%{name}
# ITK is an open-source software system to support the Visible Human Project. 
# Currently under active development, ITK employs leading-edge segmentation 
# and registration algorithms in two, three, and more dimensions.
# 
# The Insight Toolkit was developed by six principal organizations, three 
# commercial (Kitware, GE Corporate R&D, and Insightful) and three academic 
# (UNC Chapel Hill, University of Utah, and University of Pennsylvania). 
# Additional team members include Harvard Brigham & Women's Hospital, 
# University of Pittsburgh, and Columbia University. The funding for the 
# project is from the National Library of Medicine at the National Institutes 
# of Health. NLM in turn was supported by member institutions of NIH (see 
# sponsors). 


%prep
%setup -q -n InsightToolkit-%{version}
%patch10 -p0
#%patch11 -p0

# doc
bunzip2 %{SOURCE1} -c > ItkSoftwareGuide.pdf

# remove CVS dirs, if exists
find -name CVS -type d | xargs rm -rf

%build
cmake -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} \
      -DCMAKE_CXX_COMPILER:PATH=%{_bindir}/c++ \
      -DCMAKE_C_COMPILER:PATH=%{_bindir}/gcc \
      -DBUILD_SHARED_LIBS:BOOL=ON \
      -DBUILD_DOXYGEN:BOOL=ON \
      -DITK_USE_REVIEW:BOOL=ON \
      -DUSE_FFTWF:BOOL=ON \
      -DUSE_FFTWD:BOOL=ON \
      -DFFTW_INCLUDE_PATH:PATH=%{_includedir} \
      -DITK_USE_SYSTEM_TIFF:BOOL=ON \
      -DITK_USE_SYSTEM_PNG:BOOL=ON \
      -DITK_USE_SYSTEM_ZLIB:BOOL=ON \
      -DCMAKE_SKIP_RPATH:BOOL=ON \
      -DCMAKE_CXX_FLAGS:STRING="$RPM_OPT_FLAGS" \
      -DCMAKE_C_FLAGS:STRING="$RPM_OPT_FLAGS" \
.

#      -DCableSwig_DIR:PATH=%{_libdir}/CableSwig \
#      -DCMAKE_BUILD_TYPE:STRING=Release \
#      -DITK_CSWIG_TCL:BOOL=ON \
#       -DITK_CSWIG_PYTHON:BOOL=ON \
#       -DITK_USE_PYTHON_NUMARRAY:BOOL=ON \
#      -DPYTHON_INCLUDE_PATH:PATH=$PYTHON_INCLUDE_PATH \
#      -DPYTHON_LIBRARY:FILEPATH=$PYTHON_LIBRARY \
#      -DCMAKE_CXX_FLAGS:STRING=$RPM_OPT_FLAGS \
#      -DCMAKE_C_FLAGS:STRING=$RPM_OPT_FLAGS	\
      
%if %build_java
cmake	-DJAVA_INCLUDE_PATH:PATH=$JAVA_HOME/include \
	-DJAVA_INCLUDE_PATH2:PATH=$JAVA_HOME/include/linux \
	-DJAVA_AWT_INCLUDE_PATH:PATH=$JAVA_HOME/include \
	-DJAVA_AWT_LIBRARY:PATH=$JAVA_HOME/jre/lib/i386/libawt.so \
	-DVTK_WRAP_JAVA:BOOL=ON \
.
%endif

%if %build_patented
cmake 	-DITK_USE_PATENTED:BOOL=ON \
.
%endif


#      -DITK_USE_SYSTEM_VXL:BOOL=ON \
#      -DBUILD_EXAMPLES:BOOL=ON \


%make

# build docs
mkdir -p Documentation/Doxygen
doxygen doxygen.config

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

echo "build_java=%{build_java}"

make install DESTDIR=%{buildroot}

# fix lib path on x86_64
%ifarch x86_64
mv %{buildroot}/%{_prefix}/lib %{buildroot}/%{_libdir}
ls %{buildroot}/%{_libdir}/InsightToolkit/*.cmake | xargs perl -pi -e 's#/lib/#/lib64/#g'
%endif

# install ld.so.conf path
install -d -m 755 %{buildroot}/%{_sysconfdir}/ld.so.conf.d
cat > %{buildroot}/%{_sysconfdir}/ld.so.conf.d/%{name}.conf <<_EOF
%{_libdir}/InsightToolkit
_EOF

# install docs
install -d -m 755 %{buildroot}/%{_datadir}/%{name}-doc
cp -a Documentation/Doxygen/html %{buildroot}/%{_datadir}/%{name}-doc/api

# install examples
install -d -m 755 %{buildroot}/%{_datadir}/%{name}-examples/
cp -a Testing %{buildroot}/%{_datadir}/%{name}-examples/
cp -a Examples %{buildroot}/%{_datadir}/%{name}-examples/
# get rid of unwanted files
find %{buildroot}/%{_datadir}/itk-examples/ -name "*.o" -exec rm {} \;
find %{buildroot}/%{_datadir}/itk-examples/ -name CMakeCache.txt -exec rm {} \;
find %{buildroot}/%{_datadir}/itk-examples/ -name Makefile -exec rm {} \;
find %{buildroot}/%{_datadir}/itk-examples/ -name DartTestfile.txt -exec rm {} \;
find %{buildroot}/%{_datadir}/itk-examples/ -name .NoDartCoverage -exec rm {} \;
find %{buildroot}/%{_datadir}/itk-examples/ -name "cmake.*" -exec rm {} \;

#install data
mv %{buildroot}/%{_datadir}/itk-examples/Testing/Data %{buildroot}/%{_datadir}/%{name}-data

#install tcl utils
#cp Wrapping/CSwig/Tcl/itkutils.tcl %{buildroot}/%{_libdir}/InsightToolkit/tcl/
# rm -f %{buildroot}/%{_libdir}/InsightToolkit/itkwish

# multiarch support
%multiarch_includes  %{buildroot}/%{_includedir}/InsightToolkit/Utilities/itksys/FundamentalType.h


%check

# set the lib path needed to run the tests
export LD_LIBRARY_PATH=`pwd`/bin

# some tests related to the fixed filters are now wrong and must be disable
ctest -E 'itkGrayscaleMorphologicalClosingImageFilterTest|itkGrayscaleMorphologicalOpeningImageFilterTest|itkBlackTopHatImageFilterTest|itkWhiteTopHatImageFilterTest|itkClosingByReconstructionImageFilterTest|itkClosingByReconstructionImageFilterTest2|MorphologicalImageEnhancementTest|FFTDirectInverse2Test|ImageRegistration14Test|DeformableRegistration3Test'


%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif



%files -n %{libname}
%defattr(0644,root,root,0755)
%doc README.html 
%doc Documentation/DeveloperList.txt
%doc Copyright/*
%dir %{_libdir}/InsightToolkit
%{_libdir}/InsightToolkit/lib*.so.%{major}*
%{_sysconfdir}/ld.so.conf.d/%{name}.conf


%files -n %{develname}
%defattr(0644,root,root,0755)
%attr(0755,root,root) %{_bindir}/*
%{_includedir}/*
%{_libdir}/InsightToolkit/*.cmake
%{_libdir}/InsightToolkit/lib*.so

%files doc
%defattr(0644,root,root,0755)
%doc Documentation/InsightDeveloperStart.pdf
%doc Documentation/Style.pdf
%doc ItkSoftwareGuide.pdf
%{_datadir}/%{name}-doc

%files examples
%defattr(0644,root,root,0755)
%{_datadir}/%{name}-examples/Examples
%{_datadir}/%{name}-examples/Testing

%files data
%defattr(0644,root,root,0755)
%{_datadir}/%{name}-data

# %files -n python-%{name}
# %defattr(0644,root,root,0755)
# %{_libdir}/InsightToolkit/*Python.so
# %{_libdir}/InsightToolkit/python
# %{_libdir}/InsightToolkit/*.py
# %(python -c"import os,sys; print os.path.join(sys.exec_prefix, '%{_lib}', 'python' + sys.version[:3],'site-packages', 'InsightToolkit.pth')")

# %files -n tcl-%{name}
# %defattr(0644,root,root,0755)
# %attr(755,root,root) %{_bindir}/itkwish
# %{_libdir}/InsightToolkit/tcl
# %{_libdir}/InsightToolkit/*Tcl.so
# %attr(755,root,root) %{_libdir}/InsightToolkit/itkwish

%if %build_java
%files -n java-%{name}
%defattr(0644,root,root,0755)
%{_libdir}/InsightToolkit/java
%{_libdir}/InsightToolkit/*Java.so
%endif

