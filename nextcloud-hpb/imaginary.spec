Name:           imaginary
Version:        1.2.4
Release:        1%{?dist}
Summary:        Fast, simple, scalable, Docker-ready HTTP microservice for high-level image processing
License:        MIT
Group:          Applications/Internet
URL:            https://github.com/h2non/%{name}
Source0:        https://github.com/h2non/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRoot:      %{_topdir}/BUILDROOT/
BuildRequires:  systemd
BuildRequires:  glibc-devel
BuildRequires:  vips-devel
BuildRequires:  git
BuildRequires:  golang

%description
Fast HTTP microservice written in Go for high-level image processing backed by bimg and libvips. imaginary can be used as private or public HTTP service for massive image processing with first-class support for Docker & Fly.io. It's almost dependency-free and only uses net/http native package without additional abstractions for better performance.
Supports multiple image operations exposed as a simple HTTP API, with additional optional features such as API token authorization, URL signature protection, HTTP traffic throttle strategy and CORS support for web clients.

%global debug_package %{nil}

%prep
%autosetup -n %{name}-%{version}

%build
export GOTOOLCHAIN=auto
export GOSUMDB=sum.golang.org
go build -ldflags="-linkmode=external"

%install
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_sysconfdir}
mkdir -p %{buildroot}/%{_unitdir}
install -m 755 imaginary %{buildroot}/%{_bindir}/imaginary
## need to chech if can setup a systemd service

%pre
## need to chech if can setup a systemd service

%clean
rm -rf %{buildroot}

%files
%attr(755, root, root) %{_bindir}/imaginary
#attr(644, root, root) {_unitdir}/nats-server.service
#config(noreplace) {_sysconfdir}/nats-server.conf

%changelog
* Mon Nov 03 2025 Marco Bignami <m.bignami@unknown-domain.no-ip.net> 1.2.4-1
 - First iteration
