%define build_patented 0
%{?_with_patented: %{expand: %%global build_patented 1}}

%define build_examples 0
%{?_with_examples: %{expand: %%global build_examples 1}}

Name: itk
Version: 3.10.0
Release: %mkrel 1
Summary: Medicine Insight Segmentation and Registration
License: BSD-like
Group: Sciences/Other
URL: http://www.itk.org
Source0: http://ovh.dl.sourceforge.net/sourceforge/itk/InsightToolkit-%{version}.tar.gz
Source1: http://ovh.dl.sourceforge.net/sourceforge/itk/ItkSoftwareGuide-2.4.0.pdf.bz2
Patch0: SOURCES/InsightToolkit-3.10.0-build-install.patch
BuildRequires: cmake >= 2.6.0
BuildRequires: X11-devel
BuildRequires: png-devel
BuildRequires: tiff-devel
BuildRequires: zlib-devel
BuildRequires: fftw3-devel
BuildRequires: graphviz
BuildRequires: doxygen
BuildRequires: perl
BuildRequires: fontconfig
BuildRequires: java-devel
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

#---------------------------------------------------------------------------------

%define major 0
%define libname %mklibname %{name} %{major}

%package -n %{libname}
Group: System/Libraries
Summary: Medicine Insight Segmentation and Registration
Provides: %{name} = %{version}-%{release}
Provides: InsightToolkit = %{version}-%{release}

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
%dir %{_libdir}/InsightToolkit
%{_libdir}/InsightToolkit/lib*.so.%{major}*
%{_sysconfdir}/ld.so.conf.d/%{name}.conf

#---------------------------------------------------------------------------------

%define develname %mklibname %{name} -d

%package -n %{develname}
Summary: ITK header files for building C++ code
Group: Development/C++
Requires: %{libname} = %{version}
Provides: %{name}-devel = %{version}
Provides: lib%{name}-devel = %{version}

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

%files -n %{develname}
%defattr(0644,root,root,0755)
%attr(0755,root,root) %{_bindir}/*
%doc README.html 
%doc Documentation/DeveloperList.txt
%doc Copyright/*
%{_includedir}/*
%{_libdir}/InsightToolkit/*.cmake
%{_libdir}/InsightToolkit/lib*.so

#---------------------------------------------------------------------------------
%if %build_examples

%package examples
Summary: C++, Tcl and Python example programs/scripts for ITK
Group: Development/C++
Requires: %{name}-data = %{version}
Requires: %{libname} = %{version}

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

%files examples
%defattr(0644,root,root,0755)
%{_datadir}/%{name}-examples/Examples
%{_datadir}/%{name}-examples/Testing

%endif

#---------------------------------------------------------------------------------

%package data
Summary: These data are required to run various examples from the examples package
Group: Development/C++

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

%files data
%defattr(0644,root,root,0755)
%{_datadir}/%{name}-data

#---------------------------------------------------------------------------------

%package doc
Summary: Documentation for ITK
Group: Development/C++

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

%files doc
%defattr(0644,root,root,0755)
%doc Documentation/InsightDeveloperStart.pdf
%doc Documentation/Style.pdf
%doc ItkSoftwareGuide.pdf
%{_datadir}/%{name}-doc

#---------------------------------------------------------------------------------

%package -n java-%{name}
Summary: Java bindings for ITK
Group: Development/Java
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

%files -n java-%{name}
%defattr(0644,root,root,0755)
%{_libdir}/InsightToolkit/java
%{_libdir}/InsightToolkit/*Java.so

#---------------------------------------------------------------------------------

%prep
%setup -q -n InsightToolkit-%{version}

%patch0 -p0 -b build_install

# doc
bunzip2 %{SOURCE1} -c > ItkSoftwareGuide.pdf

# remove CVS dirs, if exists
find -name CVS -type d | xargs rm -rf


%build
%cmake \
    -DBUILD_DOXYGEN:BOOL=ON \
    -DITK_USE_REVIEW:BOOL=ON \
    -DUSE_FFTWF:BOOL=ON \
    -DUSE_FFTWD:BOOL=ON \
    -DFFTW_INCLUDE_PATH:PATH=%{_includedir} \
    -DITK_USE_REVIEW=OFF \
    -DBUILD_SHARED_LIBS=ON \
    -DITK_USE_SYSTEM_TIFF=ON \
    -DITK_USE_SYSTEM_PNG=ON \
    -DITK_USE_SYSTEM_ZLIB=ON \
    -DJAVA_INCLUDE_PATH=$JAVA_HOME/include \
    -DJAVA_INCLUDE_PATH2=$JAVA_HOME/include/linux \
    -DJAVA_AWT_INCLUDE_PATH=$JAVA_HOME/include \
    -DJAVA_AWT_LIBRARY=$JAVA_HOME/jre/lib/i386/libawt.so \
    %if ! %build_examples
    -DBUILD_EXAMPLES=OFF \
    %endif
    %if %build_patented
    -DITK_USE_PATENTED:BOOL=ON \
    %endif
    -DVTK_WRAP_JAVA:BOOL=ON

%make

# build docs
mkdir -p Documentation/Doxygen
doxygen Utilities/Doxygen/doxygen.config

%install
rm -rf %{buildroot}

%makeinstall_std-C build

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

# multiarch support
%multiarch_includes  %{buildroot}/%{_includedir}/InsightToolkit/Utilities/itksys/FundamentalType.h

%clean
rm -rf %{buildroot}

