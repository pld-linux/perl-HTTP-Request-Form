%define		perl_sitelib	%(eval "`perl -V:installsitelib`"; echo $installsitelib)
Summary:	HTTP-Request-Form perl module
Summary(pl):	Modu³ perla HTTP-Request-Form
Name:		perl-HTTP-Request-Form
Version:	0.4
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/HTTP/HTTP-Request-Form-%{version}.tar.gz
BuildRequires:	perl >= 5.005_03-10
BuildRequires:	perl-URI
BuildRequires:	perl-libwww
BuildRequires:	perl-HTML-Tree
%requires_eq	perl
Requires:	%{perl_sitearch}
Requires:	perl-URI
Requires:	perl-libwww
Requires:	perl-HTML-Tree
BuildRoot:	/tmp/%{name}-%{version}-root

%description
HTTP-Request-Form perl module

%description -l pl
Modu³ Perla HTTP-Request-Form

%prep
%setup -q -n HTTP-Request-Form-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/HTTP/Request/Form
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README}.gz

%{perl_sitelib}/HTTP/Request/Form.pm
%{perl_sitearch}/auto/HTTP/Request/Form

%{_mandir}/man3/*
