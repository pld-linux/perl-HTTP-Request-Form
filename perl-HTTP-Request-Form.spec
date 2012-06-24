%define	pdir	HTTP
%define	pnam	Request-Form
%include	/usr/lib/rpm/macros.perl
Summary:	HTTP-Request-Form perl module
Summary(pl):	Modu� perla HTTP-Request-Form
Name:		perl-HTTP-Request-Form
Version:	0.951
Release:	3

License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-URI
BuildRequires:	perl-libwww
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTTP-Request-Form perl module.

%description -l pl
Modu� Perla HTTP-Request-Form.

%prep
%setup -q -n HTTP-Request-Form-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/HTTP/Request/Form.pm
%{_mandir}/man3/*
