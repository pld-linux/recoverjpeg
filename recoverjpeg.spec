Summary:	JPEG files recover 
Summary(pl):	Aplikacja do odzyskiwania plików JPEG
Name:		recoverjpeg
Version:	1.0
Release:	0.1
License:	GPL
Group:		Applications/File
Source0:	http://www.rfc1149.net/download/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	394b20c88f2785fd2d008b7006261ef8
URL:		http://www.rfc1149.net/devel/recoverjpeg
Requires:	ImageMagick
Requires:	libexif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
recoverjpeg tries to recover JFIF (JPEG) pictures from a peripheral.
This may be useful if a partition is mistakenly overwriten or if a
device such as a digital camera memory card is bogus.

%description -l pl
recoverjpeg próbuje odzyskaæ z peryferia zdjêcia zapisane w formacie
JFIF (JPEG). Mo¿e to byæ u¿yteczne w przypadku omy³kowego nadpisania
partycji lub gdy no¶nik taki jak pamiêæ aparatu cyfrowego jest
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
