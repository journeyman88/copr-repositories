Name:           brotli
Version:        0.6.0
Release:        1%{?dist}
Summary:        Lossless compression algorithm
License:        MIT
URL:            https://github.com/google/brotli
Source0:        https://github.com/google/brotli/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  glibc-devel
BuildRequires:  gcc-c++
BuildRequires:  cmake

%description
Brotli is a generic-purpose lossless compression algorithm that compresses
data using a combination of a modern variant of the LZ77 algorithm, Huffman
coding and 2nd order context modeling, with a compression ratio comparable
to the best currently available general-purpose compression methods.
It is similar in speed with deflate but offers more dense compression.

%package -n %{name}-devel
Summary:        Lossless compression algorithm (development files)
Requires: %{name}%{?_isa} = %{version}-%{release} 
%description -n %{name}-devel
Brotli is a generic-purpose lossless compression algorithm that compresses
data using a combination of a modern variant of the LZ77 algorithm, Huffman
coding and 2nd order context modeling, with a compression ratio comparable
to the best currently available general-purpose compression methods.
It is similar in speed with deflate but offers more dense compression.
This package installs the development files

%prep
%autosetup -n %{name}-%{version}
%{__chmod} 644 enc/*.[ch]
%{__chmod} 644 include/brotli/*.h

%build
mkdir -p build
cd build
%cmake .. -DCMAKE_INSTALL_PREFIX="%{_prefix}" \
    -DCMAKE_INSTALL_LIBDIR="%{_libdir}"
%make_build
cd ..

%install
cd build
%make_install

%files
%{_bindir}/bro
%{_libdir}/*.so.*
%license LICENSE

%files -n %{name}-devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*

%changelog
* Thu Nov 15 2018 Marco Bignami <m.bignami@unknown-domain.no-ip.net> - 0.6.0-1
- Initial build
