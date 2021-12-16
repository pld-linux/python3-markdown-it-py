#
# Conditional build:
%bcond_with	tests	# unit tests (not included in sdist)

Summary:	Python port of markdown-it: Markdown parsing, done right
Summary(pl.UTF-8):	Pythonowy port markdown-it: analiza Markdown zrobiona dobrze
Name:		python3-markdown-it-py
Version:	2.0.0
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/markdown-it-py/
Source0:	https://files.pythonhosted.org/packages/source/m/markdown-it-py/markdown-it-py-%{version}.tar.gz
# Source0-md5:	15d36cd4a26e0febe09f8661fd487167
URL:		https://pypi.org/project/markdown-it-py/
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools >= 1:46.4.0
%if %{with tests}
BuildRequires:	python3-attrs >= 19
BuildRequires:	python3-mdurl >= 0.1
BuildRequires:	python3-pytest
BuildRequires:	python3-pytest-cov
BuildRequires:	python3-pytest-regressions
%if "%{py3_ver}" < "3.8"
BuildRequires:	python3-typing_extensions >= 3.7.4
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	sed >= 4.0
Requires:	python3-modules >= 1:3.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a Python port of markdown-it, and some of its associated
plugins.

%description -l pl.UTF-8
Ten pakiet to pythonowy port projektu markdown-it i kilku powiązanych
wtyczek.

%prep
%setup -q -n markdown-it-py-%{version}

%{__sed} -i -e '/mdurl/ s/~=/>=/' setup.cfg

%build
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE LICENSE.markdown-it README.md
%attr(755,root,root) %{_bindir}/markdown-it
%{py3_sitescriptdir}/markdown_it
%{py3_sitescriptdir}/markdown_it_py-%{version}-py*.egg-info
