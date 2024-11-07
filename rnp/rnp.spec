Name:           rnp
Version:        0.17.1
Release:        2%{?dist}
Summary:        High performance C++ OpenPGP library, fully compliant to RFC 4880
License:        BSD
Group:          Applications/Internet
URL:            https://www.rnpgp.com/
Source0:        https://github.com/rnpgp/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRoot:      %{_topdir}/BUILDROOT/
BuildRequires:  git
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libstdc++-devel
BuildRequires:  glibc-devel
BuildRequires:  json-c-devel
BuildRequires:  bzip2-devel
BuildRequires:  zlib-devel
BuildRequires:  botan2-devel
BuildRequires:  rubygem-asciidoctor
BuildRequires:	cmake

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
%autosetup -n %{name}-%{version}

%build
mkdir build
cd build
CFLAGS="${CFLAGS:-%optflags}" ; export CFLAGS
CXXFLAGS="${CXXFLAGS:-%optflags}" ; export CXXFLAGS
FFLAGS="${FFLAGS:-%optflags}" ; export FFLAGS
cmake .. -DCMAKE_INSTALL_PREFIX="" -DCMAKE_INSTALL_LIBDIR=%{_libdir} \
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
%attr(-, root, root) %{_libdir}/librnp.so
%attr(-, root, root) %{_libdir}/librnp.so.0
%attr(755, root, root) %{_libdir}/librnp.so.%{version}
%attr(-, root, root) %{_defaultdocdir}/rnp/
%attr(-, root, root) %{_mandir}/man1/rnp.1.gz
%attr(-, root, root) %{_mandir}/man1/rnpkeys.1.gz
%attr(-, root, root) %{_mandir}/man3/librnp.3.gz

%files devel
%attr(-, root, root) %{_includedir}/rnp/
%attr(-, root, root) %{_libdir}/cmake/rnp/
%attr(-, root, root) %{_libdir}/pkgconfig/librnp.pc

%changelog
* Thu Nov 7 2024 Marco Bignami <m.bignami@unknown-domain.no-ip.net> 0.17.1-2
 - Fix build spec.

* Fri Sep 20 2024 Marco Bignami <m.bignami@unknown-domain.no-ip.net> 0.17.1-1
 - Upgrade to upstream 0.17.1

* Sun Aug 06 2023 Marco Bignami <m.bignami@unknown-domain.no-ip.net> 0.17.0-1
 - Upgrade to upstream 0.17.0

* Wed Sep 28 2022 Marco Bignami <m.bignami@unknown-domain.no-ip.net> 0.16.2-1
 - Upgrade to upstream 0.16.2

* Tue Dec 07 2021 Marco Bignami <m.bignami@unknown-domain.no-ip.net> 0.15.2-3
 - Fix git builddeps

* Tue Dec 07 2021 Marco Bignami <m.bignami@unknown-domain.no-ip.net> 0.15.2-2
 - Fix asciidoctor deps

* Thu Sep 23 2021 Marco Bignami <m.bignami@unknown-domain.no-ip.net> 0.15.2-1
 - Upgrade to upstream 0.15.2

* Fri Apr 23 2021 Marco Bignami <m.bignami@unknown-domain.no-ip.net> 0.15.0-1
 - Upgrade to upstream 0.15.0

* Thu Feb 11 2021 Marco Bignami <m.bignami@unknown-domain.no-ip.net> 0.14.0-1
 - Upgrade to upstream 0.14.0

* Tue Jan 07 2020 Marco Bignami <m.bignami@unknown-domain.no-ip.net> 0.13.0-2
 - Fix in change of documentation format

* Tue Jan 07 2020 Marco Bignami <m.bignami@unknown-domain.no-ip.net> 0.13.0-1
 - Upgrade to upstream 0.13.0

* Tue Nov 12 2019 Marco Bignami <m.bignami@unknown-domain.no-ip.net> 0.12.0-1
 - Initial build package 0.12.0
