%include	/usr/lib/rpm/macros.perl
%define	pdir	HTTP
%define	pnam	Request-Form
Summary:	HTTP::Request::Form - Construct HTTP::Request objects for form processing
Name:		perl-HTTP-Request-Form
Version:	0.952
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-HTML-Tree
BuildRequires:	perl-URI
BuildRequires:	perl-libwww
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is an extension of the HTTP::Request suite. It allows easy processing
of forms in a user agent by filling out fields, querying fields,
selections and buttons and pressing buttons. It uses HTML::TreeBuilder
generated parse trees of documents (especially the forms parts extracted
with extract_links) and generates it's own internal representation of
forms from which it then generates the request objects to process the
form application.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/HTTP/Request/Form.pm
%{_mandir}/man3/*
