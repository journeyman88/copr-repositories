Name:           nextcloud-spreed-signaling
Version:        2.0.1
Release:        1%{?dist}
Summary:        The standalone signaling server which can be used for Nextcloud Talk.
License:        AGPLv3
Group:          Applications/Internet
URL:            https://janus.conf.meetecho.com/
Source0:        https://github.com/strukturag/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRoot:      %{_topdir}/BUILDROOT/
BuildRequires:  pkgconfig
BuildRequires:  libconfig-devel
BuildRequires:  libtool
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  glibc-devel
BuildRequires:  glib2-devel
BuildRequires:  openssl-devel
BuildRequires:  golang

%description
The standalone signaling server which can be used for Nextcloud Talk.

%prep
%autosetup -n %{name}-%{version}

%build
%__make %{?_smp_mflags}

%install
mkdir -p %{buildroot}/%{_bindir}
install -m 755 bin/signaling %{buildroot}/%{_bindir}/signaling-server
install -m 755 bin/proxy %{buildroot}/%{_bindir}/signaling-proxy
mkdir -p %{buildroot}/%{_defaultdocdir}/nextcloud-spreed-signaling
install -m 644 README.md %{buildroot}/%{_defaultdocdir}/nextcloud-spreed-signaling/README.md
install -m 644 LICENSE %{buildroot}/%{_defaultdocdir}/nextcloud-spreed-signaling/LICENSE
install -m 644 CHANGELOG.md %{buildroot}/%{_defaultdocdir}/nextcloud-spreed-signaling/CHANGELOG.md
install -m 644 docs/index.md %{buildroot}/%{_defaultdocdir}/nextcloud-spreed-signaling/index.md
install -m 644 docs/standalone-signaling-api-v1.md %{buildroot}/%{_defaultdocdir}/nextcloud-spreed-signaling/standalone-signaling-api-v1.md
install -m 644 docs/prometheus-metrics.md %{buildroot}/%{_defaultdocdir}/nextcloud-spreed-signaling/prometheus-metrics.md
install -m 644 docs/requirements.txt %{buildroot}/%{_defaultdocdir}/nextcloud-spreed-signaling/requirements.txt
mkdir -p %{buildroot}/%{_sysconfdir}/signaling
install -m 644 server.conf.in %{buildroot}/%{_sysconfdir}/signaling/server.conf
install -m 644 proxy.conf.in %{buildroot}/%{_sysconfdir}/signaling/proxy.conf
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

echo "[Unit]" >>  %{buildroot}/%{_unitdir}/signaling-proxy.service
echo "Nextcloud Talk signaling proxy" >>  %{buildroot}/%{_unitdir}/signaling-proxy.service
echo "After=network.target" >>  %{buildroot}/%{_unitdir}/signaling-proxy.service
echo "" >>  %{buildroot}/%{_unitdir}/signaling-proxy.service
echo "[Service]" >>  %{buildroot}/%{_unitdir}/signaling.service
echo "ExecStart=/usr/bin/signaling-proxy --config /etc/signaling/proxy.conf" >>  %{buildroot}/%{_unitdir}/signaling-proxy.service
echo "User=signaling" >>  %{buildroot}/%{_unitdir}/signaling-proxy.service
echo "Group=signaling" >>  %{buildroot}/%{_unitdir}/signaling-proxy.service
echo "Restart=on-failure" >>  %{buildroot}/%{_unitdir}/signaling-proxy.service
echo "" >>  %{buildroot}/%{_unitdir}/signaling-proxy.service
echo "[Install]" >>  %{buildroot}/%{_unitdir}/signaling-proxy.service
echo "WantedBy=multi-user.target" >>  %{buildroot}/%{_unitdir}/signaling-proxy.service

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