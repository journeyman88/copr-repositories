Name:           hiawatha
Version:        11.5
Release:        1%{?dist}
Summary:        An advanced and secure web-server for Unix
License:        GPLv2
Group:          Applications/Internet
URL:            https://www.hiawatha-webserver.org/
Source0:        https://www.hiawatha-webserver.org/files/%{name}-%{version}.tar.gz
#Source1:        https://unknown-domain.no-ip.net/pkg/hiawatha/hiawatha.service.tar.gz

BuildRoot:      %{_topdir}/BUILDROOT/
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  glibc-devel
BuildRequires:  libxml2-devel
BuildRequires:  libxslt-devel
BuildRequires:  systemd-units

%if 0%{?rhel}
BuildRequires:	cmake3
%define bldcmd	cmake3
%endif
%if 0%{?fedora}
BuildRequires:	cmake
%define bldcmd	cmake
%endif

%description
Hiawatha is a web-server with the three key attributes: secure, easy-to-use, 
and lightweight.

%package        extra
Summary:        Extra tools for Hiawatha Web Server
Group:          Applications/Internet
Requires:       %{name} = %{version}-%{release}

%description    extra
This package contains extra scripts written for Hiawatha Web Server, such as 
an integration system for Let's Encrypt.

%prep
%setup -q

%build
mkdir bld
cd bld
CFLAGS="${CFLAGS:-%optflags}" ; export CFLAGS
CXXFLAGS="${CXXFLAGS:-%optflags}" ; export CXXFLAGS
FFLAGS="${FFLAGS:-%optflags}" ; export FFLAGS
%bldcmd -DCMAKE_INSTALL_PREFIX="" -DCMAKE_INSTALL_LIBDIR=%{_libdir} \
      -DCMAKE_INSTALL_BINDIR=%{_bindir} -DCMAKE_INSTALL_SBINDIR=%{_sbindir} \
      -DCMAKE_INSTALL_SYSCONFDIR=%{_sysconfdir} -DCMAKE_INSTALL_MANDIR=%{_mandir} \
      -DENABLE_TOMAHAWK=on -DENABLE_MONITOR=on -DUSE_SYSTEM_MBEDTLS=off \
      -DENABLE_CACHE=on -DENABLE_TLS=on -DENABLE_RPROXY=on -DENABLE_XSLT=on \
      -DENABLE_LOADCHECK=on -DENABLE_TOOLKIT=on -DCMAKE_C_STANDARD=99 \
      -DUSE_STATIC_MBEDTLS_LIBRARY=on -DUSE_SHARED_MBEDTLS_LIBRARY=off ..
%__make %{?_smp_mflags}

%install
rm -rf %{buildroot}
mkdir -p  %{buildroot}
cd bld
%__make install DESTDIR=%{buildroot}
mkdir -p %{buildroot}%{_unitdir}
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d/
install -m644 logrotate.d/hiawatha %{buildroot}%{_sysconfdir}/logrotate.d/hiawatha
sed -i "s/#ServerId/ServerId/" %{buildroot}%{_sysconfdir}/hiawatha/hiawatha.conf
sed -i "s/www-data/hiawatha/" %{buildroot}%{_sysconfdir}/hiawatha/hiawatha.conf
sed -i "s/www-data www-data/hiawatha hiawatha/" %{buildroot}%{_sysconfdir}/logrotate.d/hiawatha
cd ..
install -m644 extra/debian/hiawatha.service %{buildroot}%{_unitdir}/hiawatha.service
rm -rf %{buildroot}/cmake
rm -rf %{buildroot}/include

# Docs
mkdir -p %{buildroot}%{_defaultdocdir}/hiawatha
install -m644 ChangeLog %{buildroot}%{_defaultdocdir}/hiawatha/ChangeLog
install -m644 LICENSE %{buildroot}%{_defaultdocdir}/hiawatha/LICENSE
install -m644 README.md %{buildroot}%{_defaultdocdir}/hiawatha/README.md

%pre
getent group hiawatha >/dev/null || groupadd -r hiawatha
getent passwd hiawatha >/dev/null || \
    useradd -r -g hiawatha -d /var/www/hiawatha -s /sbin/nologin \
    -c "Hiawatha Web server" hiawatha

%post
if [ "$1" = 1 ]; then
    systemctl preset hiawatha.service >/dev/null 2>&1 ||:
    systemctl start hiawatha
else
    systemctl daemon-reload
    systemctl restart hiawatha
fi
exit 0

%preun
if [ "$1" = 0 ]; then
    systemctl --no-reload disable hiawatha.service >/dev/null 2>&1 ||:
    systemctl stop hiawatha.service >/dev/null 2>&1 ||:
fi
exit 0

%clean
rm -rf %{buildroot}

%files
%attr(755, root, root) %{_bindir}/ssi-cgi
%attr(755, root, root) %{_sbindir}/cgi-wrapper
%attr(755, root, root) %{_sbindir}/hiawatha
%attr(755, root, root) %{_sbindir}/wigwam
%attr(644, root, root) %{_mandir}/man1/cgi-wrapper.1.gz
%attr(644, root, root) %{_mandir}/man1/hiawatha.1.gz
%attr(644, root, root) %{_mandir}/man1/ssi-cgi.1.gz
%attr(644, root, root) %{_mandir}/man1/wigwam.1.gz
%attr(-, root, root) %{_localstatedir}/log/hiawatha/
%attr(-, root, root) %{_localstatedir}/www/hiawatha/
%attr(-, root, root) %{_defaultdocdir}/hiawatha/
%attr(-, root, root) %{_unitdir}/
%config(noreplace) %{_sysconfdir}/hiawatha
%config(noreplace) %{_sysconfdir}/logrotate.d/hiawatha
%exclude %{_libdir}/hiawatha

%files extra
%attr(755, root, root) %{_sbindir}/lefh
%attr(-, root, root) %{_libdir}/hiawatha/letsencrypt
%attr(644, root, root) %{_mandir}/man1/lefh.1.gz

%changelog
* Thu Nov 23 2023 Marco Bignami <m.bignami@unknown-domain.no-ip.net> 11.5-1
 - Upgraded to upstream 11.5

* Sun Aug 06 2023 Marco Bignami <m.bignami@unknown-domain.no-ip.net> 11.4-1
 - Upgraded to upstream 11.4
 
* Wed Sep 28 2022 Marco Bignami <m.bignami@unknown-domain.no-ip.net> 11.2-1
 - Upgraded to upstream 11.2
 
* Tue Dec 07 2021 Marco Bignami <m.bignami@unknown-domain.no-ip.net> 11.0-2
 - Fixed spec for EPEL7 and CentOS-Stream build

* Thu Sep 23 2021 Marco Bignami <m.bignami@unknown-domain.no-ip.net> 11.0-1
 - Upgraded to upstream 11.0

* Thu Feb 11 2021 Marco Bignami <m.bignami@unknown-domain.no-ip.net> 10.11-1
 - Upgraded to upstream 10.11

* Thu Jan 23 2020 Marco Bignami <m.bignami@unknown-domain.no-ip.net> 10.10-2
 - Fix SPEC for change on upstream

* Thu Jan 23 2020 Marco Bignami <m.bignami@unknown-domain.no-ip.net> 10.10-1
 - Upgraded to upstream 10.10

* Mon Jul 30 2018 Marco Bignami <m.bignami@unknown-domain.no-ip.net> 10.8.2-1
 - Upgraded to upstream 10.8.2

* Thu Apr 12 2018 Marco Bignami <m.bignami@unknown-domain.no-ip.net> 10.8.1-1
 - Upgraded to upstream 10.8.1

* Thu Mar 22 2018 Marco Bignami <m.bignami@unknown-domain.no-ip.net> 10.8-2
 - Added compatibility macros for EL7

* Thu Mar 22 2018 Marco Bignami <m.bignami@unknown-domain.no-ip.net> 10.8-1
 - Upgraded to upstream 10.8

* Mon Oct 23 2017 Marco Bignami <m.bignami@unknown-domain.no-ip.net> 10.7-1
 - Upgraded to upstream 10.7

* Thu Apr 27 2017 Marco Bignami <m.bignami@unknown-domain.no-ip.net> 10.6-1
 - Upgraded to upstream 10.6

* Mon Jan 30 2017 Marco Bignami <m.bignami@unknown-domain.no-ip.net> 10.5-1
 - Upgraded to upstream 10.5

* Wed Nov 23 2016 Marco Bignami <m.bignami@unknown-domain.no-ip.net> 10.4-2
 - Changed init script to upstram.

* Sun Oct 09 2016 Marco Bignami <m.bignami@unknown-domain.no-ip.net> 10.4-1
 - Upgraded to upstream 10.4

* Wed Jun 22 2016 Marco Bignami <m.bignami@unknown-domain.no-ip.net> 10.3-4
 - Fixed spec for auto reload of systemd unit
 - Created extra subpackage

* Wed Jun 22 2016 Marco Bignami <m.bignami@unknown-domain.no-ip.net> 10.3-3
 - Fixed spec to use internal mbedtls

* Wed Jun 22 2016 Marco Bignami <m.bignami@unknown-domain.no-ip.net> 10.3-2
 - Added group for EPEL build

* Wed Jun 22 2016 Marco Bignami <m.bignami@unknown-domain.no-ip.net> 10.3-1
 - Fixed spec for hiawatha-10.3

* Tue Jun 21 2016 Marco Bignami <m.bignami@unknown-domain.no-ip.net> 10.3-1
 - Created spec for hiawatha-10.3
