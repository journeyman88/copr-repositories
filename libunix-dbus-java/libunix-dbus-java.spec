Name:           libunix-dbus-java
Version:        0.8.0
Release:        1%{?dist}
Summary:        Fork of Unix Sockets Library for Keycloak-SSSD
License:        LGPLv2
Group:          Development/Libraries
URL:            https://github.com/keycloak/libunix-dbus-java
Source0:        https://github.com/keycloak/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRoot:      %{_topdir}/BUILDROOT/
BuildRequires:  git
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libstdc++-devel
BuildRequires:  glibc-devel
BuildRequires:  zlib-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  java-17-openjdk-devel

%description
A Java Library to communicate at a low level with D-Bus.

%package        devel
Summary:        Development files for libunix-dbus-java.
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description    devel
A Java Library to communicate at a low level with D-Bus.

%prep
%setup -q

%build
libtoolize
aclocal
autoconf
automake --add-missing
./configure --libdir=%{_libdir} --includedir=%{_includedir}

%__make %{?_smp_mflags}

%install
rm -rf %{buildroot}
mkdir -p  %{buildroot}
%__make install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%attr(-, root, root) %{_libdir}/libunix_dbus_java.so
%attr(-, root, root) %{_libdir}/libunix_dbus_java.so.0
%attr(755, root, root) %{_libdir}/libunix_dbus_java.so.0.0.8

%files devel
%attr(-, root, root) %{_includedir}/libunix-dbus-java/

%changelog
* Thu Dec 15 2022 Marco Bignami <m.bignami@unknown-domain.no-ip.net> 0.8.0-1
 - Initial spec 0.8.0
