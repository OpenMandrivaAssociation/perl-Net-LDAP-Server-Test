
%define realname   Net-LDAP-Server-Test
%define version    0.07
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Test Net::LDAP code
Source:     http://www.cpan.org/modules/by-module/Net/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(IO::Select)
BuildRequires: perl(IO::Socket)
BuildRequires: perl(Net::LDAP)
BuildRequires: perl(Net::LDAP::Server)
BuildRequires: perl(Test::More)

BuildArch: noarch

%description
Now you can test your Net::LDAP code without having a real LDAP server
available.





%prep
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


