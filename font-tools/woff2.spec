Name:           woff2
Version:        1.0.2
Release:        1%{?dist}
Summary:        Libraries to handle woff2 fonts.
License:        ASL 2.0
Group:          Applications/File
URL:            https://github.com/google/woff2
Source0:        https://github.com/google/woff2/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRoot:      %{_topdir}/BUILDROOT/
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  glibc-devel
BuildRequires:  gcc-c++
BuildRequires:  cmake
BuildRequires:  pkgconfig(libbrotlicommon)
BuildRequires:  pkgconfig(libbrotlidec)
BuildRequires:  pkgconfig(libbrotlienc)

%description
This is a set of libraries that implements and handle the WOFF2
font file format.

%package -n %{name}-tools
Summary:        Tools to compress/decompress woff2 fonts.
Requires: %{name}%{?_isa} = %{version}-%{release} 
%description -n %{name}-tools
This is a set of tools (a compressor and a decompressor) to transform
TTF fonts to the more efficent WOFF2 format.

%package -n %{name}-devel
Summary:        Libraries to handle woff2 fonts (development files)
Requires: %{name}%{?_isa} = %{version}-%{release} 
%description -n %{name}-devel
Development files for libraries handling woff2 files.

%prep
%autosetup -n %{name}-%{version}

%build
mkdir build
cd build
CFLAGS="${CFLAGS:-%optflags}" ; export CFLAGS
CXXFLAGS="${CXXFLAGS:-%optflags} -std=c++11" ; export CXXFLAGS
FFLAGS="${FFLAGS:-%optflags}" ; export FFLAGS
%cmake .. -DCMAKE_INSTALL_PREFIX="%{_prefix}" \
    -DCMAKE_INSTALL_LIBDIR="%{_libdir}"
%make_build

%install
rm -rf %{buildroot}
mkdir -p  %{buildroot}%{_bindir}/
mkdir -p  %{buildroot}%{_defaultdocdir}/%{name}/
cd build
%make_install
install -m755 woff2_decompress %{buildroot}%{_bindir}/
install -m755 woff2_compress %{buildroot}%{_bindir}/
install -m755 woff2_info %{buildroot}%{_bindir}/
install -m644 ../README.md %{buildroot}%{_defaultdocdir}/%{name}/
install -m644 ../CONTRIBUTING.md %{buildroot}%{_defaultdocdir}/%{name}/
install -m644 ../LICENSE %{buildroot}%{_defaultdocdir}/%{name}/

%clean
rm -rf %{buildroot}

%files
%attr(644, root, root) %{_libdir}/*.so.*
%attr(-, root, root) %{_defaultdocdir}/%{name}/README.md
%attr(-, root, root) %{_defaultdocdir}/%{name}/CONTRIBUTING.md
%attr(-, root, root) %{_defaultdocdir}/%{name}/LICENSE

%files -n %{name}-tools
%attr(755, root, root) %{_bindir}/woff2_compress
%attr(755, root, root) %{_bindir}/woff2_decompress
%attr(755, root, root) %{_bindir}/woff2_info

%files -n %{name}-devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

%changelog
* Thu Nov 15 2018 Marco Bignami <m.bignami@unknown-domain.no-ip.net> 1.0.2-1
 - First build of package
