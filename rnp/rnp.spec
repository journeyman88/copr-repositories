Name:           rnp
Version:        0.13.0
Release:        2%{?dist}
Summary:        High performance C++ OpenPGP library, fully compliant to RFC 4880
License:        BSD
Group:          Applications/Internet
URL:            https://www.rnpgp.com/
Source0:        https://github.com/rnpgp/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRoot:      %{_topdir}/BUILDROOT/
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libstdc++-devel
BuildRequires:  glibc-devel
BuildRequires:  json-c-devel
BuildRequires:  bzip2-devel
BuildRequires:  zlib-devel
BuildRequires:  botan2-devel

%if 0%{?rhel}
BuildRequires:	cmake3
%define bldcmd	cmake3
%endif
%if 0%{?fedora}
BuildRequires:	cmake
%define bldcmd	cmake
%endif

%description
RNP is a set of OpenPGP (RFC4880) tools that works on Linux, *BSD and macOS as a
replacement of GnuPG. It is maintained by Ribose after being forked from 
NetPGP, itself originally written for NetBSD.

%package        devel
Summary:        Development files for RNP library.
Group:          Applications/Internet
Requires:       %{name} = %{version}-%{release}

%description    devel
LibRNP is the library used by rnp for all OpenPGP functions, useful for 
developers to build against.

%prep
%setup -q

%build
mkdir build
cd build
CFLAGS="${CFLAGS:-%optflags}" ; export CFLAGS
CXXFLAGS="${CXXFLAGS:-%optflags}" ; export CXXFLAGS
FFLAGS="${FFLAGS:-%optflags}" ; export FFLAGS
%bldcmd .. -DCMAKE_INSTALL_PREFIX="" -DCMAKE_INSTALL_LIBDIR=%{_libdir} \
      -DCMAKE_INSTALL_BINDIR=%{_bindir} -DCMAKE_INSTALL_SBINDIR=%{_sbindir} \
      -DCMAKE_INSTALL_SYSCONFDIR=%{_sysconfdir} -DCMAKE_INSTALL_MANDIR=%{_mandir} \
      -DCMAKE_INSTALL_INCLUDEDIR=/usr/include \
      -DBUILD_SHARED_LIBS=on -DBUILD_TESTING=off
%__make %{?_smp_mflags}

%install
rm -rf %{buildroot}
mkdir -p  %{buildroot}
cd build
%__make install DESTDIR=%{buildroot}
# Docs
mkdir -p %{buildroot}%{_defaultdocdir}/rnp
install -m644 ../CHANGELOG.md %{buildroot}%{_defaultdocdir}/rnp/CHANGELOG.md
install -m644 ../LICENSE.md %{buildroot}%{_defaultdocdir}/rnp/LICENSE.md
install -m644 ../LICENSE-OCB.md %{buildroot}%{_defaultdocdir}/rnp/LICENSE-OCB.md
install -m644 ../README.adoc %{buildroot}%{_defaultdocdir}/rnp/README.adoc
install -m644 ../version.txt %{buildroot}%{_defaultdocdir}/rnp/version.txt

%clean
rm -rf %{buildroot}

%files
%attr(755, root, root) %{_bindir}/rnp
%attr(755, root, root) %{_bindir}/rnpkeys
%attr(-, root, root) %{_libdir}/librnp-0.so
%attr(-, root, root) %{_libdir}/librnp-0.so.0
%attr(755, root, root) %{_libdir}/librnp-0.so.0.13.0
%attr(-, root, root) %{_defaultdocdir}/rnp/

%files devel
%attr(-, root, root) %{_includedir}/rnp-0/
%attr(-, root, root) %{_libdir}/cmake/rnp/
%attr(-, root, root) %{_libdir}/pkgconfig/librnp-0.pc

%changelog
* Tue Jan 07 2020 Marco Bignami <m.bignami@unknown-domain.no-ip.net> 0.13.0-2
 - Fix in change of documentation format

* Tue Jan 07 2020 Marco Bignami <m.bignami@unknown-domain.no-ip.net> 0.13.0-1
 - Upgrade to upstream 0.13.0

* Tue Nov 12 2019 Marco Bignami <m.bignami@unknown-domain.no-ip.net> 0.12.0-1
 - Initial build package 0.12.0
