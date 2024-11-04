Name:           nats-server
Version:        2.10.22
Release:        1%{?dist}
Summary:        The standalone signaling server which can be used for Nextcloud Talk.
License:        AGPLv3
Group:          Applications/Internet
URL:            https://janus.conf.meetecho.com/
Source0:        https://github.com/nats-io/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRoot:      %{_topdir}/BUILDROOT/
BuildRequires:  pkgconfig
BuildRequires:  libconfig-devel
BuildRequires:  libtool
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-go
BuildRequires:  glibc-devel
BuildRequires:  glib2-devel
BuildRequires:  openssl-devel
BuildRequires:  golang

%description
The standalone signaling server which can be used for Nextcloud Talk.

%prep
%autosetup -n %{name}-%{version}

%build
go build

%install
mkdir -p %{buildroot}/%{_bindir}
install -m 755 nats-server %{buildroot}/%{_bindir}/signaling-server
mkdir -p %{buildroot}/%{_unitdir}
echo "[Unit]" >>  %{buildroot}/%{_unitdir}/signaling.service
echo "Nextcloud Talk signaling server" >>  %{buildroot}/%{_unitdir}/signaling.service
echo "After=network.target" >>  %{buildroot}/%{_unitdir}/signaling.service
echo "" >>  %{buildroot}/%{_unitdir}/signaling.service
echo "[Service]" >>  %{buildroot}/%{_unitdir}/signaling.service
echo "ExecStart=/usr/bin/signaling-server --config /etc/signaling/server.conf" >>  %{buildroot}/%{_unitdir}/signaling.service
echo "User=signaling" >>  %{buildroot}/%{_unitdir}/signaling.service
echo "Group=signaling" >>  %{buildroot}/%{_unitdir}/signaling.service
echo "Restart=on-failure" >>  %{buildroot}/%{_unitdir}/signaling.service
echo "" >>  %{buildroot}/%{_unitdir}/signaling.service
echo "[Install]" >>  %{buildroot}/%{_unitdir}/signaling.service
echo "WantedBy=multi-user.target" >>  %{buildroot}/%{_unitdir}/signaling.service

%pre
getent group signaling >/dev/null || groupadd -r signaling
getent passwd signaling >/dev/null || \
    useradd -r -g signaling -d /etc/signaling -s /sbin/nologin \
    -c "Nextcloud Talk signaling server" signaling

%clean
rm -rf %{buildroot}

%files
%attr(755, root, root) %{_bindir}/signaling-server
%attr(755, root, root) %{_bindir}/signaling-proxy
%attr(-, root, root) %{_defaultdocdir}/nextcloud-spreed-signaling/
%attr(644, root, root) %{_unitdir}/signaling.service
%attr(644, root, root) %{_unitdir}/signaling-proxy.service
%config(noreplace) %{_sysconfdir}/signaling/server.conf
%config(noreplace) %{_sysconfdir}/signaling/proxy.conf

%changelog
* Sat Nov 2 2024 Marco Bignami <m.bignami@unknown-domain.no-ip.net> 1.2.4-1
 - First iteration
