%define upstream_name    Net-LDAP-Server-Test
%define upstream_version 0.19

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 0.19
Release:	1

Summary:	Test Net::LDAP code
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Net/Net-LDAP-Server-Test-0.19.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Data::Dump)
BuildRequires:	perl(IO::Select)
BuildRequires:	perl(IO::Socket)
BuildRequires:	perl(Net::LDAP)
BuildRequires:	perl(Net::LDAP::Server)
BuildRequires:	perl(Test::More)

BuildArch:	noarch

%description
Now you can test your Net::LDAP code without having a real LDAP server
available.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Mon Jun 13 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.110.0-1mdv2011.0
+ Revision: 684779
- update to new version 0.11

* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 0.100.0-2
+ Revision: 658864
- rebuild for updated spec-helper

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 0.100.0-1mdv2011.0
+ Revision: 552461
- update to 0.10

* Thu Feb 18 2010 Jérôme Quelin <jquelin@mandriva.org> 0.90.0-1mdv2010.1
+ Revision: 507586
- update to 0.09

* Fri Aug 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.80.0-1mdv2010.0
+ Revision: 421874
- adding missing buildrequires:
- update to 0.08

* Tue Aug 04 2009 Jérôme Quelin <jquelin@mandriva.org> 0.70.0-1mdv2010.0
+ Revision: 408967
- rebuild using %%perl_convert_version

* Sun Jul 19 2009 Buchan Milne <bgmilne@mandriva.org> 0.07-1mdv2010.0
+ Revision: 397927
- import perl-Net-LDAP-Server-Test


* Sun Jul 19 2009 Buchan Milne <bgmilne@mandriva.org> 0.07-1mdv
- initial mdv release, generated with cpan2dist


