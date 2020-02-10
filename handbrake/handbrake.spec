Name:           HandBrake
Version:        1.3.1
Release:        1%{?dist}
Summary:        An advanced and secure web-server for Unix
License:        GPLv2
Group:          Applications/Internet
URL:            https://handbrake.fr/
Source0:        https://github.com/HandBrake/HandBrake/releases/download/%{version}/%{name}-%{version}-source.tar.bz2
Patch1:         https://raw.githubusercontent.com/journeyman88/copr-repositories/master/handbrake/HandBrake-qsv.patch

BuildRoot:      %{_topdir}/BUILDROOT/
BuildRequires:  glibc-devel
BuildRequires:  bzip2-devel
BuildRequires:  cmake
BuildRequires:  fontconfig-devel
BuildRequires:  freetype-devel
BuildRequires:  fribidi-devel
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  harfbuzz-devel
BuildRequires:  jansson-devel
BuildRequires:  lame-devel
BuildRequires:  lbzip2
BuildRequires:  libass-devel
BuildRequires:  libogg-devel
BuildRequires:  libsamplerate-devel
BuildRequires:  libtheora-devel
BuildRequires:  libtool
BuildRequires:  libvorbis-devel
BuildRequires:  libxml2-devel
BuildRequires:  libvpx-devel
BuildRequires:  m4
BuildRequires:  make
BuildRequires:  meson
BuildRequires:  nasm
BuildRequires:  ninja-build
BuildRequires:  numactl-devel
BuildRequires:  opus-devel
BuildRequires:  patch
BuildRequires:  python
BuildRequires:  speex-devel
BuildRequires:  tar
BuildRequires:  xz-devel
BuildRequires:  zlib-devel
BuildRequires:  x264-devel
BuildRequires:  libva-devel
BuildRequires:  libdrm-devel
BuildRequires:  x265-devel
BuildRequires:  libdvdnav-devel
BuildRequires:  ffmpeg-devel
BuildRequires:  libbluray-devel
BuildRequires:  libdav1d-devel
BuildRequires:  nv-codec-headers
BuildRequires:  gettext-devel
BuildRequires:  gtk3-devel
BuildRequires:  intel-mediasdk-devel

%description
HandBrake is a tool for converting video from nearly any format to a 
selection of modern, widely supported codecs.

%define lang_subpkg() \
%package langpack-%{1}\
Summary:       %{2} language data for %{name}\
BuildArch:     noarch\
Requires:      %{name} = %{version}-%{release}\
Supplements:   (%{name} = %{version}-%{release} and langpacks-%{1})\
\
%description langpack-%{1}\
%{2} language data for %{name}.\
\
%files langpack-%{1}\
%{_datadir}/locale/%{1}/LC_MESSAGES/ghb.mo

%prep
%autosetup -p1

%build
# Use system libraries in place of bundled ones
for module in libdav1d libdvdnav libdvdread libbluray libmfx x265 nvenc ffmpeg; do
    sed -i -e "/MODULES += contrib\/$module/d" make/include/main.defs
done

echo "GCC.args.O.speed = %{optflags} `pkg-config x265 dav1d dvdread dvdnav ffnvcodec libavcodec libavdevice libavfilter libavformat libavutil libpostproc libswresample libswscale libmfx --libs --cflags`" > custom.defs
echo "GCC.args.g.none = " >> custom.defs
echo "GCC.args.strip = " >> custom.defs
CFLAGS="${CFLAGS:-%optflags}" ; export CFLAGS
CXXFLAGS="${CXXFLAGS:-%optflags}" ; export CXXFLAGS
FFLAGS="${FFLAGS:-%optflags}" ; export FFLAGS
./configure --enable-x265 --enable-numa --enable-nvenc --enable-qsv --harden --prefix=/usr
cd build
%__make %{?_smp_mflags}

%install
rm -rf %{buildroot}
mkdir -p  %{buildroot}
%__make --directory=build install DESTDIR=%{buildroot}
# Docs
mkdir -p %{buildroot}%{_defaultdocdir}/HandBrake
install -m644 AUTHORS.markdown %{buildroot}%{_defaultdocdir}/HandBrake/AUTHORS.md
install -m644 LICENSE %{buildroot}%{_defaultdocdir}/HandBrake/LICENSE
install -m644 README.markdown %{buildroot}%{_defaultdocdir}/HandBrake/README.md
install -m644 CODE_OF_CONDUCT.md %{buildroot}%{_defaultdocdir}/HandBrake/CODE_OF_CONDUCT.md
install -m644 CONTRIBUTING.md %{buildroot}%{_defaultdocdir}/HandBrake/CONTRIBUTING.md
install -m644 COPYING %{buildroot}%{_defaultdocdir}/HandBrake/COPYING
install -m644 NEWS.markdown %{buildroot}%{_defaultdocdir}/HandBrake/NEWS.md
install -m644 SECURITY.md %{buildroot}%{_defaultdocdir}/HandBrake/SECURITY.md
install -m644 THANKS.markdown %{buildroot}%{_defaultdocdir}/HandBrake/THANKS.md
install -m644 TRANSLATION.markdown %{buildroot}%{_defaultdocdir}/HandBrake/TRANSLATION.md
install -m644 version.txt %{buildroot}%{_defaultdocdir}/HandBrake/version.txt

%find_lang ghb

%lang_subpkg af Afrikaans
%lang_subpkg cs Czech
%lang_subpkg da Danish
%lang_subpkg de German
%lang_subpkg es Spanish
%lang_subpkg eu Basque
%lang_subpkg fr French
%lang_subpkg hr Croatian
%lang_subpkg it Italian
%lang_subpkg ja Japanese
%lang_subpkg ko Korean
%lang_subpkg nl Dutch
%lang_subpkg no Norwegian
%lang_subpkg pl Polish
%lang_subpkg pt_BR Brazilian Portuguese
%lang_subpkg pt Portuguese
%lang_subpkg ro Romanian
%lang_subpkg ru Russian
%lang_subpkg sk Slovak
%lang_subpkg sv Swedish
%lang_subpkg th Thai
%lang_subpkg tr Turkish
%lang_subpkg uk_UA Ukrainian
%lang_subpkg zh_CN Chinese

%clean
rm -rf %{buildroot}

%files -f ghb.lang
%attr(755, root, root) %{_bindir}/ghb
%attr(755, root, root) %{_bindir}/HandBrakeCLI
%attr(644, root, root) %{_datadir}/applications/fr.handbrake.ghb.desktop
%attr(644, root, root) %{_datadir}/metainfo/fr.handbrake.ghb.appdata.xml
%attr(644, root, root) %{_datadir}/icons/hicolor/scalable/apps/fr.handbrake.ghb.svg
%attr(644, root, root) %{_datadir}/icons/hicolor/scalable/apps/hb-icon.svg
%attr(-, root, root) %{_defaultdocdir}/HandBrake/

%changelog
* Sun Feb 09 2020 Marco Bignami <m.bignami@unknown-domain.no-ip.net> 1.3.1-1
 - Initial build
