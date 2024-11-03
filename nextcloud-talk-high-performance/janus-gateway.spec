Name:           janus-gateway
Version:        1.2.4
Release:        3%{?dist}
Summary:        Janus WebRTC Server
License:        GPLv3
Group:          Applications/Internet
URL:            https://janus.conf.meetecho.com/
Source0:        https://github.com/meetecho/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRoot:      %{_topdir}/BUILDROOT/
BuildRequires:  pkgconfig
BuildRequires:  libconfig-devel
BuildRequires:  libtool
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  glibc-devel
BuildRequires:  glib2-devel
BuildRequires:  libnice-devel
BuildRequires:  openssl-devel
BuildRequires:  libsrtp-devel
BuildRequires:  jansson-devel
BuildRequires:  doxygen
BuildRequires:  graphviz
BuildRequires:  systemd-units
BuildRequires:  usrsctp-devel
BuildRequires:  libmicrohttpd-devel
BuildRequires:  libwebsockets-devel
BuildRequires:  librabbitmq-devel
BuildRequires:  paho-c-devel
BuildRequires:  nanomsg-devel
BuildRequires:  libcurl-devel
BuildRequires:  sofia-sip-devel
BuildRequires:  opus-devel
BuildRequires:  libogg-devel
BuildRequires:  lua-devel
BuildRequires:  duktape-devel

%description
Janus is an open source, general purpose, WebRTC server designed and 
developed by Meetecho.

%package        devel
Summary:        Development files for the Janus WebRTC server
Group:          Applications/Internet
Requires:       %{name} = %{version}-%{release}

%description    devel
Janus is an open source, general purpose, WebRTC server designed and
developed by Meetecho.

%package        transport-http
Summary:        REST (HTTP/HTTPS) transport support for the Janus WebRTC server
Group:          Applications/Internet
Requires:       %{name} = %{version}-%{release}

%description    transport-http
This package contains libraries for REST (HTTP/HTTPS) transport support for Janus WebRTC server.

%package        transport-websockets
Summary:        WebSockets transport support for the Janus WebRTC server
Group:          Applications/Internet
Requires:       %{name} = %{version}-%{release}

%description    transport-websockets
This package contains libraries for WebSockets transport support for Janus WebRTC server.

%package        transport-rabbitmq
Summary:        RabbitMQ support for the Janus WebRTC server
Group:          Applications/Internet
Requires:       %{name} = %{version}-%{release}

%description    transport-rabbitmq
This package contains libraries for RabbitMQ transport support for Janus WebRTC server.

%package        transport-mqtt
Summary:        MQTT support for the Janus WebRTC server
Group:          Applications/Internet
Requires:       %{name} = %{version}-%{release}

%description    transport-mqtt
This package contains libraries for MQTT transport support for Janus WebRTC server.

%package        transport-pfunix
Summary:        Unix Sockets transport support for the Janus WebRTC server
Group:          Applications/Internet
Requires:       %{name} = %{version}-%{release}

%description    transport-pfunix
This package contains libraries for Unix Sockets transport support for Janus WebRTC server.

%package        transport-nanomsg
Summary:        Nanomsq support for the Janus WebRTC server
Group:          Applications/Internet
Requires:       %{name} = %{version}-%{release}

%description    transport-nanomsg
This package contains libraries for Nanomsg transport support for Janus WebRTC server.

%package        eventhandler-sample
Summary:        Sample EventHandler for the Janus WebRTC server
Group:          Applications/Internet
Requires:       %{name} = %{version}-%{release}

%description    eventhandler-sample
This package contains libraries for Sample EventHandler for Janus WebRTC server.

%package        eventhandler-websockets
Summary:        WebSockets EventHandler for the Janus WebRTC server
Group:          Applications/Internet
Requires:       %{name} = %{version}-%{release}

%description    eventhandler-websockets
This package contains libraries for WebSockets EventHandler for Janus WebRTC server.

%package        eventhandler-rabbitmq
Summary:        RabbitMQ EventHandler for the Janus WebRTC server
Group:          Applications/Internet
Requires:       %{name} = %{version}-%{release}

%description    eventhandler-rabbitmq
This package contains libraries for RabbitMQ EventHandler for Janus WebRTC server.

%package        eventhandler-mqtt
Summary:        MQTT EventHandler for the Janus WebRTC server
Group:          Applications/Internet
Requires:       %{name} = %{version}-%{release}

%description    eventhandler-mqtt
This package contains libraries for MQTT EventHandler for Janus WebRTC server.

%package        eventhandler-nanomsg
Summary:        Nanomsq EventHandler for the Janus WebRTC server
Group:          Applications/Internet
Requires:       %{name} = %{version}-%{release}

%description    eventhandler-nanomsg
This package contains libraries for Nanomsg EventHandler for Janus WebRTC server.

%package        eventhandler-gelf
Summary:        GELF EventHandler for the Janus WebRTC server
Group:          Applications/Internet
Requires:       %{name} = %{version}-%{release}

%description    eventhandler-gelf
This package contains libraries for GELF EventHandler for Janus WebRTC server.

%package        plugin-echotest
Summary:        Echo Test plugin for the Janus WebRTC server
Group:          Applications/Internet
Requires:       %{name} = %{version}-%{release}

%description    plugin-echotest
This package contains the Echo Test plugin for Janus WebRTC server.

%package        plugin-streaming
Summary:        Streaming plugin for the Janus WebRTC server
Group:          Applications/Internet
Requires:       %{name} = %{version}-%{release}

%description    plugin-streaming
This package contains the Streaming plugin for Janus WebRTC server.

%package        plugin-videocall
Summary:        Video Call plugin for the Janus WebRTC server
Group:          Applications/Internet
Requires:       %{name} = %{version}-%{release}

%description    plugin-videocall
This package contains the Video Call plugin for Janus WebRTC server.

%package        plugin-sip
Summary:        SIP Gateway plugin for the Janus WebRTC server
Group:          Applications/Internet
Requires:       %{name} = %{version}-%{release}

%description    plugin-sip
This package contains the SIP Gateway plugin for Janus WebRTC server.

%package        plugin-nosip
Summary:        NoSIP (RTP Bridge) plugin for the Janus WebRTC server
Group:          Applications/Internet
Requires:       %{name} = %{version}-%{release}

%description    plugin-nosip
This package contains the NoSIP (RTP Bridge) plugin for Janus WebRTC server.

%package        plugin-audiobridge
Summary:        Audio Bridge plugin for the Janus WebRTC server
Group:          Applications/Internet
Requires:       %{name} = %{version}-%{release}

%description    plugin-audiobridge
This package contains the Audio Bridge plugin for Janus WebRTC server.

%package        plugin-videoroom
Summary:        Vidoe Room plugin for the Janus WebRTC server
Group:          Applications/Internet
Requires:       %{name} = %{version}-%{release}

%description    plugin-videoroom
This package contains the Audio Bridge plugin for Janus WebRTC server.

%package        plugin-recordplay
Summary:        Record & Play plugin for the Janus WebRTC server
Group:          Applications/Internet
Requires:       %{name} = %{version}-%{release}

%description    plugin-recordplay
This package contains the Record & Play plugin for Janus WebRTC server.

%package        plugin-textroom
Summary:        Text Room plugin for the Janus WebRTC server
Group:          Applications/Internet
Requires:       %{name} = %{version}-%{release}

%description    plugin-textroom
This package contains the Text Room plugin for Janus WebRTC server.

%package        plugin-lua
Summary:        Lua plugin for the Janus WebRTC server
Group:          Applications/Internet
Requires:       %{name} = %{version}-%{release}

%description    plugin-lua
This package contains the Lua Interpeter plugin for Janus WebRTC server.

%package        plugin-duktape
Summary:        Duktape plugin for the Janus WebRTC server
Group:          Applications/Internet
Requires:       %{name} = %{version}-%{release}

%description    plugin-duktape
This package contains the Duktape Interpeter plugin for Janus WebRTC server.

%package        logger-json
Summary:        JSON external logger for the Janus WebRTC server
Group:          Applications/Internet
Requires:       %{name} = %{version}-%{release}

%description    logger-json
This package contains the JSON external logger for Janus WebRTC server.

%prep
%autosetup -n %{name}-%{version}
sh autogen.sh

%build
%configure --enable-plugin-lua --enable-plugin-duktape --enable-docs --enable-json-logger
%__make %{?_smp_mflags}

%install
%__make install DESTDIR=%{buildroot}
cd %{buildroot}/%{_sysconfdir}/janus/
for i in *.jcfg.sample; do {
    mv $i ${i/.jcfg.sample/.jcfg}
};
done
mkdir -p %{buildroot}/%{_unitdir}
echo "[Unit]" >>  %{buildroot}/%{_unitdir}/janus.service
echo "Description=Janus WebRTC gateway" >>  %{buildroot}/%{_unitdir}/janus.service
echo "After=network.target" >>  %{buildroot}/%{_unitdir}/janus.service
echo "Documentation=https://janus.conf.meetecho.com/docs/index.html" >>  %{buildroot}/%{_unitdir}/janus.service
echo "" >>  %{buildroot}/%{_unitdir}/janus.service
echo "[Service]" >>  %{buildroot}/%{_unitdir}/janus.service
echo "Type=forking" >>  %{buildroot}/%{_unitdir}/janus.service
echo "ExecStart=/usr/bin/janus --disable-colors --daemon --log-stdout" >>  %{buildroot}/%{_unitdir}/janus.service
echo "Restart=on-failure" >>  %{buildroot}/%{_unitdir}/janus.service
echo "LimitNOFILE=65536" >>  %{buildroot}/%{_unitdir}/janus.service
echo "" >>  %{buildroot}/%{_unitdir}/janus.service
echo "[Install]" >>  %{buildroot}/%{_unitdir}/janus.service
echo "WantedBy=multi-user.target" >>  %{buildroot}/%{_unitdir}/janus.service

%clean
rm -rf %{buildroot}

%files
%attr(755, root, root) %{_bindir}/janus
%attr(755, root, root) %{_bindir}/janus-cfgconv
%dir %attr(755, root, root) %{_libdir}/janus/plugins/
%dir %attr(755, root, root) %{_libdir}/janus/transports/
%dir %attr(755, root, root) %{_libdir}/janus/events/
%dir %attr(755, root, root) %{_libdir}/janus/loggers/
%attr(644, root, root) %{_mandir}/man1/janus.1.gz
%attr(644, root, root) %{_mandir}/man1/janus-cfgconv.1.gz
%attr(-, root, root) %{_defaultdocdir}/janus-gateway/
%attr(-, root, root) %{_datarootdir}/janus/
%attr(644, root, root) %{_unitdir}/janus.service
%config(noreplace) %{_sysconfdir}/janus/janus.jcfg

%files devel
%attr(-, root, root) %{_includedir}/janus/

%files transport-http
%define modname http
%define modtype transport
%define modfolder transports
%config(noreplace) %{_sysconfdir}/janus/janus.%{modtype}.%{modname}.jcfg
%attr(-, root, root) %{_libdir}/janus/%{modfolder}/libjanus_%{modname}.so
%attr(-, root, root) %{_libdir}/janus/%{modfolder}/libjanus_%{modname}.so.2
%attr(755, root, root) %{_libdir}/janus/%{modfolder}/libjanus_%{modname}.so.2.0.4
%define has_la %( if [ -f %{buildroot}/%{_libdir}/janus/%{modfolder}/libjanus_%{modname}.la ]; then echo "1" ; else echo "0"; fi )
%if %has_la
%attr(755, root, root) %{buildroot}/%{_libdir}/janus/%{modfolder}/libjanus_%{modname}.la
%endif

%files transport-websockets
%define modname websockets
%define modtype transport
%define modfolder transports
%config(noreplace) %{_sysconfdir}/janus/janus.%{modtype}.%{modname}.jcfg
%attr(-, root, root) %{_libdir}/janus/%{modfolder}/libjanus_%{modname}.so
%attr(-, root, root) %{_libdir}/janus/%{modfolder}/libjanus_%{modname}.so.2
%attr(755, root, root) %{_libdir}/janus/%{modfolder}/libjanus_%{modname}.so.2.0.4
%define has_la %( if [ -f %{buildroot}/%{_libdir}/janus/%{modfolder}/libjanus_%{modname}.la ]; then echo "1" ; else echo "0"; fi )
%if %has_la
%attr(755, root, root) %{buildroot}/%{_libdir}/janus/%{modfolder}/libjanus_%{modname}.la
%endif

%files transport-rabbitmq
%define modname rabbitmq
%define modtype transport
%define modfolder transports
%config(noreplace) %{_sysconfdir}/janus/janus.%{modtype}.%{modname}.jcfg
%attr(-, root, root) %{_libdir}/janus/%{modfolder}/libjanus_%{modname}.so
%attr(-, root, root) %{_libdir}/janus/%{modfolder}/libjanus_%{modname}.so.2
%attr(755, root, root) %{_libdir}/janus/%{modfolder}/libjanus_%{modname}.so.2.0.4
%define has_la %( if [ -f %{buildroot}/%{_libdir}/janus/%{modfolder}/libjanus_%{modname}.la ]; then echo "1" ; else echo "0"; fi )
%if %has_la
%attr(755, root, root) %{buildroot}/%{_libdir}/janus/%{modfolder}/libjanus_%{modname}.la
%endif

%files transport-mqtt
%define modname mqtt
%define modtype transport
%define modfolder transports
%config(noreplace) %{_sysconfdir}/janus/janus.%{modtype}.%{modname}.jcfg
%attr(-, root, root) %{_libdir}/janus/%{modfolder}/libjanus_%{modname}.so
%attr(-, root, root) %{_libdir}/janus/%{modfolder}/libjanus_%{modname}.so.2
%attr(755, root, root) %{_libdir}/janus/%{modfolder}/libjanus_%{modname}.so.2.0.4
%define has_la %( if [ -f %{buildroot}/%{_libdir}/janus/%{modfolder}/libjanus_%{modname}.la ]; then echo "1" ; else echo "0"; fi )
%if %has_la
%attr(755, root, root) %{buildroot}/%{_libdir}/janus/%{modfolder}/libjanus_%{modname}.la
%endif

%files transport-pfunix
%define modname pfunix
%define modtype transport
%define modfolder transports
%config(noreplace) %{_sysconfdir}/janus/janus.%{modtype}.%{modname}.jcfg
%attr(-, root, root) %{_libdir}/janus/%{modfolder}/libjanus_%{modname}.so
%attr(-, root, root) %{_libdir}/janus/%{modfolder}/libjanus_%{modname}.so.2
%attr(755, root, root) %{_libdir}/janus/%{modfolder}/libjanus_%{modname}.so.2.0.4
%define has_la %( if [ -f %{buildroot}/%{_libdir}/janus/%{modfolder}/libjanus_%{modname}.la ]; then echo "1" ; else echo "0"; fi )
%if %has_la
%attr(755, root, root) %{buildroot}/%{_libdir}/janus/%{modfolder}/libjanus_%{modname}.la
%endif

%files transport-nanomsg
%define modname nanomsg
%define modtype transport
%define modfolder transports
%config(noreplace) %{_sysconfdir}/janus/janus.%{modtype}.%{modname}.jcfg
%attr(-, root, root) %{_libdir}/janus/%{modfolder}/libjanus_%{modname}.so
%attr(-, root, root) %{_libdir}/janus/%{modfolder}/libjanus_%{modname}.so.2
%attr(755, root, root) %{_libdir}/janus/%{modfolder}/libjanus_%{modname}.so.2.0.4
%define has_la %( if [ -f %{buildroot}/%{_libdir}/janus/%{modfolder}/libjanus_%{modname}.la ]; then echo "1" ; else echo "0"; fi )
%if %has_la
%attr(755, root, root) %{buildroot}/%{_libdir}/janus/%{modfolder}/libjanus_%{modname}.la
%endif

%files eventhandler-sample
%define modname sampleevh
%define modtype eventhandler
%define modfolder events
%config(noreplace) %{_sysconfdir}/janus/janus.%{modtype}.%{modname}.jcfg
%attr(-, root, root) %{_libdir}/janus/%{modfolder}/libjanus_%{modname}.so
%attr(-, root, root) %{_libdir}/janus/%{modfolder}/libjanus_%{modname}.so.2
%attr(755, root, root) %{_libdir}/janus/%{modfolder}/libjanus_%{modname}.so.2.0.4
%define has_la %( if [ -f %{buildroot}/%{_libdir}/janus/%{modfolder}/libjanus_%{modname}.la ]; then echo "1" ; else echo "0"; fi )
%if %has_la
%attr(755, root, root) %{buildroot}/%{_libdir}/janus/%{modfolder}/libjanus_%{modname}.la
%endif

%files eventhandler-websockets
%define modname wsevh
%define modtype eventhandler
%define modfolder events
%config(noreplace) %{_sysconfdir}/janus/janus.%{modtype}.%{modname}.jcfg
%attr(-, root, root) %{_libdir}/janus/%{modfolder}/libjanus_%{modname}.so
%attr(-, root, root) %{_libdir}/janus/%{modfolder}/libjanus_%{modname}.so.2
%attr(755, root, root) %{_libdir}/janus/%{modfolder}/libjanus_%{modname}.so.2.0.4
%define has_la %( if [ -f %{buildroot}/%{_libdir}/janus/%{modfolder}/libjanus_%{modname}.la ]; then echo "1" ; else echo "0"; fi )
%if %has_la
%attr(755, root, root) %{buildroot}/%{_libdir}/janus/%{modfolder}/libjanus_%{modname}.la
%endif

%files eventhandler-rabbitmq
%define modname rabbitmqevh
%define modtype eventhandler
%define modfolder events
%config(noreplace) %{_sysconfdir}/janus/janus.%{modtype}.%{modname}.jcfg
%attr(-, root, root) %{_libdir}/janus/%{modfolder}/libjanus_%{modname}.so
%attr(-, root, root) %{_libdir}/janus/%{modfolder}/libjanus_%{modname}.so.2
%attr(755, root, root) %{_libdir}/janus/%{modfolder}/libjanus_%{modname}.so.2.0.4
%define has_la %( if [ -f %{buildroot}/%{_libdir}/janus/%{modfolder}/libjanus_%{modname}.la ]; then echo "1" ; else echo "0"; fi )
%if %has_la
%attr(755, root, root) %{buildroot}/%{_libdir}/janus/%{modfolder}/libjanus_%{modname}.la
%endif

%files eventhandler-mqtt
%define modname mqttevh
%define modtype eventhandler
%define modfolder events
%config(noreplace) %{_sysconfdir}/janus/janus.%{modtype}.%{modname}.jcfg
%attr(-, root, root) %{_libdir}/janus/%{modfolder}/libjanus_%{modname}.so
%attr(-, root, root) %{_libdir}/janus/%{modfolder}/libjanus_%{modname}.so.2
%attr(755, root, root) %{_libdir}/janus/%{modfolder}/libjanus_%{modname}.so.2.0.4
%define has_la %( if [ -f %{buildroot}/%{_libdir}/janus/%{modfolder}/libjanus_%{modname}.la ]; then echo "1" ; else echo "0"; fi )
%if %has_la
%attr(755, root, root) %{buildroot}/%{_libdir}/janus/%{modfolder}/libjanus_%{modname}.la
%endif

%files eventhandler-nanomsg
%define modname nanomsgevh
%define modtype eventhandler
%define modfolder events
%config(noreplace) %{_sysconfdir}/janus/janus.%{modtype}.%{modname}.jcfg
%attr(-, root, root) %{_libdir}/janus/%{modfolder}/libjanus_%{modname}.so
%attr(-, root, root) %{_libdir}/janus/%{modfolder}/libjanus_%{modname}.so.2
%attr(755, root, root) %{_libdir}/janus/%{modfolder}/libjanus_%{modname}.so.2.0.4
%define has_la %( if [ -f %{buildroot}/%{_libdir}/janus/%{modfolder}/libjanus_%{modname}.la ]; then echo "1" ; else echo "0"; fi )
%if %has_la
%attr(755, root, root) %{buildroot}/%{_libdir}/janus/%{modfolder}/libjanus_%{modname}.la
%endif

%files eventhandler-gelf
%define modname gelfevh
%define modtype eventhandler
%define modfolder events
%config(noreplace) %{_sysconfdir}/janus/janus.%{modtype}.%{modname}.jcfg
%attr(-, root, root) %{_libdir}/janus/%{modfolder}/libjanus_%{modname}.so
%attr(-, root, root) %{_libdir}/janus/%{modfolder}/libjanus_%{modname}.so.2
%attr(755, root, root) %{_libdir}/janus/%{modfolder}/libjanus_%{modname}.so.2.0.4
%define has_la %( if [ -f %{buildroot}/%{_libdir}/janus/%{modfolder}/libjanus_%{modname}.la ]; then echo "1" ; else echo "0"; fi )
%if %has_la
%attr(755, root, root) %{buildroot}/%{_libdir}/janus/%{modfolder}/libjanus_%{modname}.la
%endif

%files plugin-echotest
%define modname echotest
%define modtype plugin
%define modfolder plugins
%config(noreplace) %{_sysconfdir}/janus/janus.%{modtype}.%{modname}.jcfg
%attr(-, root, root) %{_libdir}/janus/%{modfolder}/libjanus_%{modname}.so
%attr(-, root, root) %{_libdir}/janus/%{modfolder}/libjanus_%{modname}.so.2
%attr(755, root, root) %{_libdir}/janus/%{modfolder}/libjanus_%{modname}.so.2.0.4
%define has_la %( if [ -f %{buildroot}/%{_libdir}/janus/%{modfolder}/libjanus_%{modname}.la ]; then echo "1" ; else echo "0"; fi )
%if %has_la
%attr(755, root, root) %{buildroot}/%{_libdir}/janus/%{modfolder}/libjanus_%{modname}.la
%endif

%files plugin-streaming
%define modname streaming
%define modtype plugin
%define modfolder plugins
%config(noreplace) %{_sysconfdir}/janus/janus.%{modtype}.%{modname}.jcfg
%attr(-, root, root) %{_libdir}/janus/%{modfolder}/libjanus_%{modname}.so
%attr(-, root, root) %{_libdir}/janus/%{modfolder}/libjanus_%{modname}.so.2
%attr(755, root, root) %{_libdir}/janus/%{modfolder}/libjanus_%{modname}.so.2.0.4
%define has_la %( if [ -f %{buildroot}/%{_libdir}/janus/%{modfolder}/libjanus_%{modname}.la ]; then echo "1" ; else echo "0"; fi )
%if %has_la
%attr(755, root, root) %{buildroot}/%{_libdir}/janus/%{modfolder}/libjanus_%{modname}.la
%endif

%files plugin-videocall
%define modname videocall
%define modtype plugin
%define modfolder plugins
%config(noreplace) %{_sysconfdir}/janus/janus.%{modtype}.%{modname}.jcfg
%attr(-, root, root) %{_libdir}/janus/%{modfolder}/libjanus_%{modname}.so
%attr(-, root, root) %{_libdir}/janus/%{modfolder}/libjanus_%{modname}.so.2
%attr(755, root, root) %{_libdir}/janus/%{modfolder}/libjanus_%{modname}.so.2.0.4
%define has_la %( if [ -f %{buildroot}/%{_libdir}/janus/%{modfolder}/libjanus_%{modname}.la ]; then echo "1" ; else echo "0"; fi )
%if %has_la
%attr(755, root, root) %{buildroot}/%{_libdir}/janus/%{modfolder}/libjanus_%{modname}.la
%endif

%files plugin-sip
%define modname sip
%define modtype plugin
%define modfolder plugins
%config(noreplace) %{_sysconfdir}/janus/janus.%{modtype}.%{modname}.jcfg
%attr(-, root, root) %{_libdir}/janus/%{modfolder}/libjanus_%{modname}.so
%attr(-, root, root) %{_libdir}/janus/%{modfolder}/libjanus_%{modname}.so.2
%attr(755, root, root) %{_libdir}/janus/%{modfolder}/libjanus_%{modname}.so.2.0.4
%define has_la %( if [ -f %{buildroot}/%{_libdir}/janus/%{modfolder}/libjanus_%{modname}.la ]; then echo "1" ; else echo "0"; fi )
%if %has_la
%attr(755, root, root) %{buildroot}/%{_libdir}/janus/%{modfolder}/libjanus_%{modname}.la
%endif

%files plugin-nosip
%define modname nosip
%define modtype plugin
%define modfolder plugins
%config(noreplace) %{_sysconfdir}/janus/janus.%{modtype}.%{modname}.jcfg
%attr(-, root, root) %{_libdir}/janus/%{modfolder}/libjanus_%{modname}.so
%attr(-, root, root) %{_libdir}/janus/%{modfolder}/libjanus_%{modname}.so.2
%attr(755, root, root) %{_libdir}/janus/%{modfolder}/libjanus_%{modname}.so.2.0.4
%define has_la %( if [ -f %{buildroot}/%{_libdir}/janus/%{modfolder}/libjanus_%{modname}.la ]; then echo "1" ; else echo "0"; fi )
%if %has_la
%attr(755, root, root) %{buildroot}/%{_libdir}/janus/%{modfolder}/libjanus_%{modname}.la
%endif

%files plugin-audiobridge
%define modname audiobridge
%define modtype plugin
%define modfolder plugins
%config(noreplace) %{_sysconfdir}/janus/janus.%{modtype}.%{modname}.jcfg
%attr(-, root, root) %{_libdir}/janus/%{modfolder}/libjanus_%{modname}.so
%attr(-, root, root) %{_libdir}/janus/%{modfolder}/libjanus_%{modname}.so.2
%attr(755, root, root) %{_libdir}/janus/%{modfolder}/libjanus_%{modname}.so.2.0.4
%define has_la %( if [ -f %{buildroot}/%{_libdir}/janus/%{modfolder}/libjanus_%{modname}.la ]; then echo "1" ; else echo "0"; fi )
%if %has_la
%attr(755, root, root) %{buildroot}/%{_libdir}/janus/%{modfolder}/libjanus_%{modname}.la
%endif

%files plugin-videoroom
%define modname videoroom
%define modtype plugin
%define modfolder plugins
%config(noreplace) %{_sysconfdir}/janus/janus.%{modtype}.%{modname}.jcfg
%attr(-, root, root) %{_libdir}/janus/%{modfolder}/libjanus_%{modname}.so
%attr(-, root, root) %{_libdir}/janus/%{modfolder}/libjanus_%{modname}.so.2
%attr(755, root, root) %{_libdir}/janus/%{modfolder}/libjanus_%{modname}.so.2.0.4
%define has_la %( if [ -f %{buildroot}/%{_libdir}/janus/%{modfolder}/libjanus_%{modname}.la ]; then echo "1" ; else echo "0"; fi )
%if %has_la
%attr(755, root, root) %{buildroot}/%{_libdir}/janus/%{modfolder}/libjanus_%{modname}.la
%endif

%files plugin-recordplay
%define modname recordplay
%define modtype plugin
%define modfolder plugins
%config(noreplace) %{_sysconfdir}/janus/janus.%{modtype}.%{modname}.jcfg
%attr(-, root, root) %{_libdir}/janus/%{modfolder}/libjanus_%{modname}.so
%attr(-, root, root) %{_libdir}/janus/%{modfolder}/libjanus_%{modname}.so.2
%attr(755, root, root) %{_libdir}/janus/%{modfolder}/libjanus_%{modname}.so.2.0.4
%define has_la %( if [ -f %{buildroot}/%{_libdir}/janus/%{modfolder}/libjanus_%{modname}.la ]; then echo "1" ; else echo "0"; fi )
%if %has_la
%attr(755, root, root) %{buildroot}/%{_libdir}/janus/%{modfolder}/libjanus_%{modname}.la
%endif

%files plugin-textroom
%define modname textroom
%define modtype plugin
%define modfolder plugins
%config(noreplace) %{_sysconfdir}/janus/janus.%{modtype}.%{modname}.jcfg
%attr(-, root, root) %{_libdir}/janus/%{modfolder}/libjanus_%{modname}.so
%attr(-, root, root) %{_libdir}/janus/%{modfolder}/libjanus_%{modname}.so.2
%attr(755, root, root) %{_libdir}/janus/%{modfolder}/libjanus_%{modname}.so.2.0.4
%define has_la %( if [ -f %{buildroot}/%{_libdir}/janus/%{modfolder}/libjanus_%{modname}.la ]; then echo "1" ; else echo "0"; fi )
%if %has_la
%attr(755, root, root) %{buildroot}/%{_libdir}/janus/%{modfolder}/libjanus_%{modname}.la
%endif

%files plugin-lua
%define modname lua
%define modtype plugin
%define modfolder plugins
%config(noreplace) %{_sysconfdir}/janus/janus.%{modtype}.%{modname}.jcfg
%attr(-, root, root) %{_libdir}/janus/%{modfolder}/libjanus_%{modname}.so
%attr(-, root, root) %{_libdir}/janus/%{modfolder}/libjanus_%{modname}.so.2
%attr(755, root, root) %{_libdir}/janus/%{modfolder}/libjanus_%{modname}.so.2.0.4
%define has_la %( if [ -f %{buildroot}/%{_libdir}/janus/%{modfolder}/libjanus_%{modname}.la ]; then echo "1" ; else echo "0"; fi )
%if %has_la
%attr(755, root, root) %{buildroot}/%{_libdir}/janus/%{modfolder}/libjanus_%{modname}.la
%endif

%files plugin-duktape
%define modname duktape
%define modtype plugin
%define modfolder plugins
%config(noreplace) %{_sysconfdir}/janus/janus.%{modtype}.%{modname}.jcfg
%attr(-, root, root) %{_libdir}/janus/%{modfolder}/libjanus_%{modname}.so
%attr(-, root, root) %{_libdir}/janus/%{modfolder}/libjanus_%{modname}.so.2
%attr(755, root, root) %{_libdir}/janus/%{modfolder}/libjanus_%{modname}.so.2.0.4
%define has_la %( if [ -f %{buildroot}/%{_libdir}/janus/%{modfolder}/libjanus_%{modname}.la ]; then echo "1" ; else echo "0"; fi )
%if %has_la
%attr(755, root, root) %{buildroot}/%{_libdir}/janus/%{modfolder}/libjanus_%{modname}.la
%endif

%files logger-json
%define modname jsonlog
%define modtype logger
%define modfolder loggers
%config(noreplace) %{_sysconfdir}/janus/janus.%{modtype}.%{modname}.jcfg
%attr(-, root, root) %{_libdir}/janus/%{modfolder}/libjanus_%{modname}.so
%attr(-, root, root) %{_libdir}/janus/%{modfolder}/libjanus_%{modname}.so.2
%attr(755, root, root) %{_libdir}/janus/%{modfolder}/libjanus_%{modname}.so.2.0.4
%define has_la %( if [ -f %{buildroot}/%{_libdir}/janus/%{modfolder}/libjanus_%{modname}.la ]; then echo "1" ; else echo "0"; fi )
%if %has_la
%attr(755, root, root) %{buildroot}/%{_libdir}/janus/%{modfolder}/libjanus_%{modname}.la
%endif

%changelog
* Sun Nov 3 2024 Marco Bignami <m.bignami@unknown-domain.no-ip.net> 1.2.4-3
 - Updated spec to handle epel

* Sat Nov 2 2024 Marco Bignami <m.bignami@unknown-domain.no-ip.net> 1.2.4-1
 - First iteration
