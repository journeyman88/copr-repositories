%define srcname notify_push
Name:           nextcloud-notify-push
Version:        0.7.0
Release:        1%{?dist}
Summary:        The standalone signaling server which can be used for Nextcloud Talk.
License:        AGPLv3
Group:          Applications/Internet
URL:            https://github.com/nextcloud/notify_push
Source0:        https://github.com/nextcloud/%{srcname}/archive/v%{version}.tar.gz#/%{srcname}-%{version}.tar.gz

BuildRoot:      %{_topdir}/BUILDROOT/
BuildRequires:  systemd
BuildRequires:  glibc-devel
BuildRequires:  rust

%description
The standalone signaling server which can be used for Nextcloud Talk.

%global debug_package %{nil}

%prep
%autosetup -n %{srcname}-%{version}

%build
cargo build --release

%install
mkdir -p %{buildroot}/%{_bindir}
install -m 755 target/release/notify_push %{buildroot}/%{_bindir}/notify_push
mkdir -p %{buildroot}/%{_defaultdocdir}/nextcloud-notify-push
install -m 644 README.md %{buildroot}/%{_defaultdocdir}/nextcloud-notify-push/README.md
install -m 644 LICENSE %{buildroot}/%{_defaultdocdir}/nextcloud-notify-push/LICENSE
install -m 644 DEVELOPING.md %{buildroot}/%{_defaultdocdir}/nextcloud-notify-push/DEVELOPING.md
install -m 644 AUTHORS.md %{buildroot}/%{_defaultdocdir}/nextcloud-notify-push/AUTHORS.md
mkdir -p %{buildroot}/%{_sysconfdir}/default
echo "PORT=7867" >> %{buildroot}/%{_sysconfdir}/default/notify-push
echo "NEXTCLOUD_DIR=/var/www/netcloud" >> %{buildroot}/%{_sysconfdir}/default/notify-push
mkdir -p %{buildroot}/%{_unitdir}
echo "[Unit]" >>  %{buildroot}/%{_unitdir}/notify-push.service
echo "Description = Push daemon for Nextcloud clients" >>  %{buildroot}/%{_unitdir}/notify-push.service
echo "Documentation=https://github.com/nextcloud/notify_push" >>  %{buildroot}/%{_unitdir}/notify-push.service
echo "" >>  %{buildroot}/%{_unitdir}/notify-push.service
echo "[Service]" >>  %{buildroot}/%{_unitdir}/notify-push.service
echo "# Change if you already have something running on this port" >>  %{buildroot}/%{_unitdir}/notify-push.service
echo "EnvironmentFile=%{_sysconfdir}/default/notify-push" >>  %{buildroot}/%{_unitdir}/notify-push.service
echo "ExecStart = %{_bindir}/notify_push \${NEXTCLOUD_DIR}/config/config.php" >>  %{buildroot}/%{_unitdir}/notify-push.service
echo "# requires the push server to have been build with the systemd feature (enabled by default)" >>  %{buildroot}/%{_unitdir}/notify-push.service
echo "Type=notify" >>  %{buildroot}/%{_unitdir}/notify-push.service
echo "" >>  %{buildroot}/%{_unitdir}/notify-push.service
echo "[Install]" >>  %{buildroot}/%{_unitdir}/notify-push.service
echo "WantedBy = multi-user.target" >>  %{buildroot}/%{_unitdir}/notify-push.service

%clean
rm -rf %{buildroot}

%files
%attr(755, root, root) %{_bindir}/notify_push
%attr(-, root, root) %{_defaultdocdir}/nextcloud-notify-push/
%attr(644, root, root) %{_unitdir}/notify-push.service
%config(noreplace) %{_sysconfdir}/default/notify-push

%changelog
* Thu Nov 7 2024 Marco Bignami <m.bignami@unknown-domain.no-ip.net> 0.7.0-1
 - First iteration
