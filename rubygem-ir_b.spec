#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-ir_b
Version  : 1.5.0
Release  : 7
URL      : https://rubygems.org/downloads/ir_b-1.5.0.gem
Source0  : https://rubygems.org/downloads/ir_b-1.5.0.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : ruby
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-rr
BuildRequires : rubygem-shoulda
BuildRequires : rubygem-test-unit

%description
ir_b
====
irb anywhere by calling 'ir b' (need a whitespace!).
Install
----
gem install ir_b

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n ir_b-1.5.0
gem spec %{SOURCE0} -l --ruby > rubygem-ir_b.gemspec

%build
gem build rubygem-ir_b.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
ir_b-1.5.0.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd %{buildroot}%{gem_dir}/gems/ir_b-1.5.0
ruby -v -I.:lib:test test*/test_*.rb || :
popd


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/ir_b-1.5.0.gem
/usr/lib64/ruby/gems/2.3.0/gems/ir_b-1.5.0/.document
/usr/lib64/ruby/gems/2.3.0/gems/ir_b-1.5.0/.gitignore
/usr/lib64/ruby/gems/2.3.0/gems/ir_b-1.5.0/Gemfile
/usr/lib64/ruby/gems/2.3.0/gems/ir_b-1.5.0/LICENSE
/usr/lib64/ruby/gems/2.3.0/gems/ir_b-1.5.0/README.md
/usr/lib64/ruby/gems/2.3.0/gems/ir_b-1.5.0/Rakefile
/usr/lib64/ruby/gems/2.3.0/gems/ir_b-1.5.0/VERSION
/usr/lib64/ruby/gems/2.3.0/gems/ir_b-1.5.0/examples/example1.rb
/usr/lib64/ruby/gems/2.3.0/gems/ir_b-1.5.0/examples/example2.rb
/usr/lib64/ruby/gems/2.3.0/gems/ir_b-1.5.0/examples/with_pry.rb
/usr/lib64/ruby/gems/2.3.0/gems/ir_b-1.5.0/ir_b.gemspec
/usr/lib64/ruby/gems/2.3.0/gems/ir_b-1.5.0/lib/ir_b.rb
/usr/lib64/ruby/gems/2.3.0/gems/ir_b-1.5.0/lib/ir_b/pry-remote-auto.rb
/usr/lib64/ruby/gems/2.3.0/gems/ir_b-1.5.0/lib/ir_b/pry-remote.rb
/usr/lib64/ruby/gems/2.3.0/gems/ir_b-1.5.0/lib/ir_b/pry.rb
/usr/lib64/ruby/gems/2.3.0/gems/ir_b-1.5.0/test/helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/ir_b-1.5.0/test/test_ir_b.rb
/usr/lib64/ruby/gems/2.3.0/specifications/ir_b-1.5.0.gemspec
