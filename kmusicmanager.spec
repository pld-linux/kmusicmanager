Summary:	KMusicManager manages your entire music collection.
Summary(pl):	KMusicManager pomaga w zarz±dzaniu zasobami muzycznymi
Name:		kmusicmanager
Version:	1.2
#%define	bver	pre2
Release:	0.1
License:	GPL
Group:		Multimedia
Source0:	http://peterhost.dl.sourceforge.net/sourceforge/kmusicmanager/kmusicmanager-1.2.tar.gz
#Source1:	%{name}.desktop
# Source0-md5:	738f882b952b7cf6318a6295f2f00e2d
URL:		http://kmusicmanager.sourceforge.net/index.html
BuildRequires:	taglib-devel >= 1.3
BuildRequires:	kdebase-devel >= 3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KMusicManager's main features are :
- Manages your music collection of MP3, Ogg-Vorbis and FLAC files.
- Monitors directories for new songs.
- You can edit the tags of your songs.
- Create playlists, using drag and drop.
- You can choose what KMusicManager plays next by dragging and dropping songs into the play queue.

%description -l pl
G³ównymi mo¿liwo¶ciami programu KMusicPlayer s±:
- zarz±dzanie kolekcjami muzycznimi w formacie mp3, ogg-vorbis, flac
- obserwacja katalogów w poszukiwaniu nowym piosenek
- edycja opisów piosenek
- tworzenie playlist metod± przeci±gania myszk±


%prep
%setup -q -n %{name}-%{version}

%configure

%build
make

%install
make install

#install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

install src/hi32-app-kmusicmanager.png $RPM_BUILD_ROOT%{_pixmapsdir}/kmusicmanager.png

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(644,root,root,755)
%doc README LICENSE AUTHORS COPYING
