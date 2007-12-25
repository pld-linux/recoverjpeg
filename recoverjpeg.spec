Summary:	JPEG files recover 
Summary(pl.UTF-8):	Aplikacja do odzyskiwania plików JPEG
Name:		recoverjpeg
Version:	1.1.2
Release:	0.1
License:	GPL
Group:		Applications/File
Source0:	http://www.rfc1149.net/download/recoverjpeg/%{name}-%{version}.tar.gz
# Source0-md5:	3bb054f4dfba25a6291a39f81706052a
URL:		http://www.rfc1149.net/devel/recoverjpeg/
Requires:	ImageMagick
Requires:	exif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
recoverjpeg tries to recover JFIF (JPEG) pictures from a peripheral.
This may be useful if a partition is mistakenly overwriten or if a
device such as a digital camera memory card is bogus.

%description -l pl.UTF-8
recoverjpeg próbuje odzyskać z peryferia zdjęcia zapisane w formacie
JFIF (JPEG). Może to być użyteczne w przypadku omyłkowego nadpisania
partycji lub gdy nośnik taki jak pamięć aparatu cyfrowego jest
uszkodzony.

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
%doc README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
