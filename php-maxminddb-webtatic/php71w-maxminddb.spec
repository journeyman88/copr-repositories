#
# spec file for package phalcon

%global altName MaxMind-DB-Reader-php
#%global debug_package %{nil}

Name:           php71w-maxminddb
Summary:        MaxMind DB Reader extension
Version:        1.4.1
Release:        1
License:        ASL 2.0
Group:          Development/Libraries
Url:            https://github.com/maxmind/MaxMind-DB-Reader-php
Source0:        https://github.com/maxmind/%{altName}/archive/v%{version}.tar.gz#/%{altName}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{altName}-%{version}
Requires:       php71w-common
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  php71w-devel
BuildRequires:  libtool
BuildRequires:  pcre-devel
BuildRequires:  libmaxminddb-devel

%description
MaxMind DB is a binary file format that stores data indexed by
IP address subnets (IPv4 or IPv6).
This optional PHP C Extension is a drop-in replacement for
MaxMind\Db\Reader.
Databases are available in geolite2-country and geolite2-city packages.

%prep
%autosetup -n %{altName}-%{version}


%build
cp -R ext ext-zts
cd ext
phpize
CFLAGS="${CFLAGS:-%optflags}" ; export CFLAGS
CXXFLAGS="${CXXFLAGS:-%optflags}" ; export CXXFLAGS
FFLAGS="${FFLAGS:-%optflags}" ; export FFLAGS
./configure --with-php-config=/usr/bin/php-config
make
cd ../ext-zts
zts-phpize
CFLAGS="${CFLAGS:-%optflags}" ; export CFLAGS
CXXFLAGS="${CXXFLAGS:-%optflags}" ; export CXXFLAGS
FFLAGS="${FFLAGS:-%optflags}" ; export FFLAGS
./configure --with-php-config=/usr/bin/zts-php-config
make

%install
mkdir -p %{buildroot}%{_defaultdocdir}/php-maxminddb/
install -m644 CHANGELOG.md %{buildroot}%{_defaultdocdir}/php-maxminddb/
install -m644 LICENSE %{buildroot}%{_defaultdocdir}/php-maxminddb/
install -m644 README.md %{buildroot}%{_defaultdocdir}/php-maxminddb/
cd ext
make INSTALL_ROOT=%{buildroot} install
mkdir -p %{buildroot}%{_sysconfdir}/php.d/
echo "extension=maxminddb.so" > %{buildroot}%{_sysconfdir}/php.d/20-maxminddb.ini
cd ../ext-zts
make INSTALL_ROOT=%{buildroot} install
mkdir -p %{buildroot}%{_sysconfdir}/php-zts.d/
echo "extension=maxminddb.so" > %{buildroot}%{_sysconfdir}/php-zts.d/20-maxminddb.ini

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%attr(755, root, root) %{_libdir}/php/modules/maxminddb.so
%attr(644, root, root) %{_sysconfdir}/php.d/20-maxminddb.ini
%attr(755, root, root) %{_libdir}/php-zts/modules/maxminddb.so
%attr(644, root, root) %{_sysconfdir}/php-zts.d/20-maxminddb.ini
%attr(755, root, root) %{_defaultdocdir}/php-maxminddb/

%changelog
* Wed Mar 20 2019 Marco Bignami <m.bignami@unknown-domain.no-ip.net> 1.4.1-1
 - Created package.
