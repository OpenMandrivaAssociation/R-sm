%global packname  sm
%global rlibdir  %{_datadir}/R/library

Name:             R-%{packname}
Version:          2.2_4.1
Release:          2
Summary:          Smoothing methods for nonparametric regression and density estimation
Group:            Sciences/Mathematics
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2.2-4.1.tar.gz
BuildArch:        noarch
Requires:         R-core
Requires:         R-rpanel R-tkrplot R-rgl R-misc3d R-akima R-gam 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex 
BuildRequires:    R-rpanel R-tkrplot R-rgl R-misc3d R-akima R-gam 

%description
This is software linked to the book `Applied Smoothing Techniques for Data
Analysis: The Kernel Approach with S-Plus Illustrations' Oxford University

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

# FIXME (possibly due to bootstrap of other packages: Error in rgl.open() : rgl.open failed)
%if 0
%check
%{_bindir}/R CMD check %{packname}
%endif

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/history.txt
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/COPYING
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/scripts
%{rlibdir}/%{packname}/smdata
