Summary:	JPEG files recover 
Summary(pl.UTF-8):	Aplikacja do odzyskiwania plików JPEG
Name:		recoverjpeg
Version:	2.3
Release:	1
License:	GPL v2
Group:		Applications/File
Source0:	http://www.rfc1149.net/download/recoverjpeg/%{name}-%{version}.tar.gz
# Source0-md5:	54a36482a6bb4ec1214995fc06be27bb
URL:		http://www.rfc1149.net/devel/recoverjpeg/
BuildRequires:	libstdc++-devel
Requires:	ImageMagick
Requires:	exif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
recoverjpeg tries to recover JFIF (JPEG) pictures from a peripheral.
This may be useful if a partition is mistakenly overwriten or if a
device such as a digital camera memory card is bogus.

%description -l pl.UTF-8
recoverjpeg próbuje odzyskać zdjęcia zapisane w formacie JFIF (JPEG).
Może to być użyteczne w przypadku omyłkowego nadpisania partycji lub
gdy nośnik taki jak pamięć aparatu cyfrowego jest uszkodzony.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_bindir}/recoverjpeg
%attr(755,root,root) %{_bindir}/recovermov
%attr(755,root,root) %{_bindir}/remove-duplicates
%attr(755,root,root) %{_bindir}/sort-pictures
%{_mandir}/man1/recoverjpeg.1*
%{_mandir}/man1/recovermov.1*
%{_mandir}/man1/remove-duplicates.1*
%{_mandir}/man1/sort-pictures.1*
