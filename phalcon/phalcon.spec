#
# spec file for package phalcon

%global altName cphalcon
%global debug_package %{nil}

Name:           phalcon
Summary:        High performance, full-stack PHP framework delivered as a C extension.
Version:        3.4.1
Release:        1
License:        GPLv2+
Group:          Applications/Productivity
Url:            https://phalconphp.com/
Source0:        https://github.com/phalcon/%{altName}/archive/v%{version}.tar.gz#/%{altName}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{altName}-%{version}
Requires:       php-common
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  php-devel
BuildRequires:  libtool
BuildRequires:  pcre-devel
BuildRequires:  re2c
BuildRequires:  sed

%description
Phalcon is an open source full stack framework for PHP, written 
as a C-extension. Phalcon is optimized for high performance. 
Its unique architecture allows the framework to always be memory 
resident, offering its functionality whenever its needed, 
without expensive file stats and file reads that traditional 
PHP frameworks employ.

%prep
%autosetup -n %{altName}-%{version}


%build
cd build
sed -e '/^make/ d' -e '/Thanks/ d' -e '/^export CFL/ d' <install > copr-builder && echo "make -s -j\"$(getconf _NPROCESSORS_ONLN)\"" >> copr-builder
sed -e '/^make/ d' -e '/Thanks/ d' -e '/^export CFL/ d' <install > copr-installer && echo "make -s install" >> copr-installer
chmod +x copr-*
CFLAGS="${CFLAGS:-%optflags}" ; export CFLAGS
CXXFLAGS="${CXXFLAGS:-%optflags}" ; export CXXFLAGS
FFLAGS="${FFLAGS:-%optflags}" ; export FFLAGS
./copr-builder

%install
cd build
export INSTALL_ROOT=%{buildroot} && ./copr-installer
mkdir -p %{buildroot}%{_sysconfdir}/php.d/
echo "extension=phalcon.so" > %{buildroot}%{_sysconfdir}/php.d/20-phalcon.ini

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%attr(755, root, root) %{_libdir}/php/modules/phalcon.so
%attr(644, root, root) %{_sysconfdir}/php.d/20-phalcon.ini
%attr(644, root, root) %{_includedir}/php/ext/phalcon/

%changelog
* Fri Nov 16 2018 Marco Bignami <m.bignami@unknown-domain.no-ip.net> 3.4.1-1
 - Created spec file
