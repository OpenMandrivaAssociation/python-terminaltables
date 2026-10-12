Name:		python-terminaltables
Version:	3.1.10
Release:	2
Summary:	Generate simple tables in terminals from a nested list of strings
License:	MIT
Group:		Development/Python
URL:		https://pypi.org/project/terminaltables/
Source0:	terminaltables-3.1.10.tar.gz
BuildSystem:	python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(setuptools)
BuildArch:	noarch

%prep -a
rm -f pyproject.toml
%description
Generate simple tables in terminals from a nested list of strings.

%files
%{py_sitedir}/*
