# TODO: desktop file
Summary:	KMusicManager manages your entire music collection.
Summary(pl):	KMusicManager pomaga w zarz±dzaniu zasobami muzycznymi
Name:		kmusicmanager
Version:	1.2
Release:	0.1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://dl.sourceforge.net/kmusicmanager/%{name}-%{version}.tar.gz
# Source0-md5:	738f882b952b7cf6318a6295f2f00e2d
URL:		http://kmusicmanager.sourceforge.net/index.html
BuildRequires:	automake
BuildRequires:	kdebase-devel >= 3
BuildRequires:	taglib-devel >= 1.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KMusicManager's main features are :
- Manages your music collection of MP3, Ogg-Vorbis and FLAC files.
- Monitors directories for new songs.
- You can edit the tags of your songs.
- Create playlists, using drag and drop.
- You can choose what KMusicManager plays next by dragging and
  dropping songs into the play queue.

%description -l pl
G³ównymi mo¿liwo¶ciami programu KMusicManager s±:
- zarz±dzanie kolekcjami muzycznymi w formacie MP3, Ogg-Vorbis, FLAC
- obserwacja katalogów w poszukiwaniu nowym piosenek
- edycja opisów piosenek
- tworzenie playlist metod± przeci±gania myszk±

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub admin
%configure \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_pixmapsdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

#install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

install src/hi32-app-kmusicmanager.png $RPM_BUILD_ROOT%{_pixmapsdir}/kmusicmanager.png

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%{_pixmapsdir}/*.png
%{_iconsdir}/*/*/*/*.png
%{_datadir}/apps/%{name}
