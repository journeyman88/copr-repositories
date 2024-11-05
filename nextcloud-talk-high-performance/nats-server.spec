Name:           nats-server
Version:        2.10.22
Release:        1%{?dist}
Summary:        The standalone signaling server which can be used for Nextcloud Talk.
License:        AGPLv3
Group:          Applications/Internet
URL:            https://janus.conf.meetecho.com/
Source0:        https://github.com/nats-io/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRoot:      %{_topdir}/BUILDROOT/
BuildRequires:  glibc-devel
BuildRequires:  golang

%description
The standalone signaling server which can be used for Nextcloud Talk.

%global debug_package %{nil}

%prep
%autosetup -n %{name}-%{version}

%build
go build -ldflags="-linkmode=external"

%install
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_sysconfdir}
mkdir -p %{buildroot}/%{_unitdir}
mkdir -p %{buildroot}/%{_localstatedir}/nats-server
install -m 755 nats-server %{buildroot}/%{_bindir}/nats-server
echo "host: 127.0.0.1" >> %{buildroot}/%{_sysconfdir}/nats-server.conf
echo "port: 4222" >> %{buildroot}/%{_sysconfdir}/nats-server.conf
echo "[Unit]" >> %{buildroot}/%{_unitdir}/nats-server.service
echo "Description=NATS Server" >> %{buildroot}/%{_unitdir}/nats-server.service
echo "After=network-online.target ntp.service" >> %{buildroot}/%{_unitdir}/nats-server.service
echo "" >> %{buildroot}/%{_unitdir}/nats-server.service
echo "[Service]" >> %{buildroot}/%{_unitdir}/nats-server.service
echo "Type=simple" >> %{buildroot}/%{_unitdir}/nats-server.service
echo "ExecStart=/usr/bin/nats-server -c /etc/nats-server.conf" >> %{buildroot}/%{_unitdir}/nats-server.service
echo "ExecReload=/bin/kill -s HUP $MAINPID" >> %{buildroot}/%{_unitdir}/nats-server.service
echo "ExecStop=/bin/kill -s SIGINT $MAINPID" >> %{buildroot}/%{_unitdir}/nats-server.service
echo "" >> %{buildroot}/%{_unitdir}/nats-server.service
echo "User=nats" >> %{buildroot}/%{_unitdir}/nats-server.service
echo "Group=nats" >> %{buildroot}/%{_unitdir}/nats-server.service
echo "" >> %{buildroot}/%{_unitdir}/nats-server.service
echo "Restart=always" >> %{buildroot}/%{_unitdir}/nats-server.service
echo "RestartSec=5" >> %{buildroot}/%{_unitdir}/nats-server.service
echo "# The nats-server uses SIGUSR2 to trigger using Lame Duck Mode (LDM) shutdown" >> %{buildroot}/%{_unitdir}/nats-server.service
echo "KillSignal=SIGUSR2" >> %{buildroot}/%{_unitdir}/nats-server.service
echo "# You might want to adjust TimeoutStopSec too." >> %{buildroot}/%{_unitdir}/nats-server.service
echo "" >> %{buildroot}/%{_unitdir}/nats-server.service
echo "# Capacity Limits" >> %{buildroot}/%{_unitdir}/nats-server.service
echo "# JetStream requires 2 FDs open per stream." >> %{buildroot}/%{_unitdir}/nats-server.service
echo "LimitNOFILE=800000" >> %{buildroot}/%{_unitdir}/nats-server.service

%pre
getent group nats >/dev/null || groupadd -r nats
getent passwd nats >/dev/null || \
    useradd -r -g nats -d %{_localstatedir}/nats-server -s /sbin/nologin \
    -c "NATS server" nats

%clean
rm -rf %{buildroot}

%files
%attr(755, root, root) %{_bindir}/nats-server
%attr(644, root, root) %{_unitdir}/nats-server.service
%config(noreplace) %{_sysconfdir}/nats-server.conf
%dir %attr(644, nats, nats) %{_localstatedir}/nats-server

%changelog
* Tue Nov 5 2024 Marco Bignami <m.bignami@unknown-domain.no-ip.net> 2.10.22-1
 - First iteration
