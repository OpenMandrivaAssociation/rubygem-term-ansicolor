%define oname term-ansicolor

Summary:    Ruby library that colors strings using ANSI escape sequences
Name:       rubygem-%{oname}
Version:    1.0.7
Release:	2
Group:      Development/Ruby
License:    GPLv2+
URL:        http://flori.github.com/term-ansicolor
Source0:    http://rubygems.org/gems/%{oname}-%{version}.gem
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}
Requires:   rubygems
BuildRequires: rubygems
BuildArch:  noarch
Provides:   rubygem(%{oname}) = %{version}

%description
Ruby library that colors strings using ANSI escape sequences

%prep

%build

%install
mkdir -p %{buildroot}%{ruby_gemdir}
gem install --local --install-dir %{buildroot}%{ruby_gemdir} \
            --force --rdoc %{SOURCE0}
mkdir -p %{buildroot}/%{_bindir}
mv %{buildroot}%{ruby_gemdir}/bin/* %{buildroot}/%{_bindir}
rmdir %{buildroot}%{ruby_gemdir}/bin
find %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/bin -type f | xargs chmod 755
chmod a-x %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/{CHANGES,COPYING,VERSION,README.rdoc}
chmod g-w %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/{examples,tests}/*.rb
chmod g-w %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/{Rakefile,install.rb}

rm -rf %{buildroot}%{ruby_gemdir}/gems//%{oname}-%{version}/.gitignore

%files
%{_bindir}/cdiff
%{_bindir}/decolor
%dir %{ruby_gemdir}/gems/%{oname}-%{version}/
%{ruby_gemdir}/gems/%{oname}-%{version}/install.rb
%{ruby_gemdir}/gems/%{oname}-%{version}/bin/
%{ruby_gemdir}/gems/%{oname}-%{version}/examples/
%{ruby_gemdir}/gems/%{oname}-%{version}/lib/
%{ruby_gemdir}/gems/%{oname}-%{version}/tests/
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/CHANGES
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/COPYING
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/VERSION
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/Rakefile
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/*.txt
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/*.rdoc
%{ruby_gemdir}/gems/%{oname}-%{version}/*.gemspec
%{ruby_gemdir}/gems/%{oname}-%{version}/Gemfile
%{ruby_gemdir}/gems/%{oname}-%{version}/Gemfile
%{ruby_gemdir}/gems/%{oname}-%{version}/.travis.yml
%{ruby_gemdir}/cache/%{oname}-%{version}.gem
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec
