%include	/usr/lib/rpm/macros.perl
Summary:	HTTP-Request-Form perl module
Summary(pl):	Modu³ perla HTTP-Request-Form
Name:		perl-HTTP-Request-Form
Version:	0.7
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/HTTP/HTTP-Request-Form-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-URI
BuildRequires:	perl-libwww
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTTP-Request-Form perl module.

%description -l pl
Modu³ Perla HTTP-Request-Form.

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
