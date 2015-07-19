# revision 23085
# category TLCore
# catalog-ctan /language/hyphenation/tkhyph.tex
# catalog-date 2011-02-23 08:51:21 +0100
# catalog-license other-free
# catalog-version undef
Name:		texlive-hyphen-turkish
Version:	20110223
Release:	11
Summary:	Turkish hyphenation patterns
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/hyphenation/tkhyph.tex
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-turkish.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-hyphen-base
Requires:	texlive-hyph-utf8

%description
Hyphenation patterns for Turkish in T1/EC and UTF-8 encodings.
The patterns for Turkish were first produced for the Ottoman
Texts Project in 1987 and were suitable for both Modern Turkish
and Ottoman Turkish in Latin script, however the required
character set didn't fit into EC encoding, so support for
Ottoman Turkish had to be dropped to keep compatibility with 8-
bit engines.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%_texmf_language_dat_d/hyphen-turkish
%_texmf_language_def_d/hyphen-turkish
%_texmf_language_lua_d/hyphen-turkish

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/hyphen-turkish <<EOF
\%% from hyphen-turkish:
turkish loadhyph-tr.tex
EOF
perl -pi -e 's|\\%%|%%|;' %{buildroot}%{_texmf_language_dat_d}/hyphen-turkish
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/hyphen-turkish <<EOF
\%% from hyphen-turkish:
\addlanguage{turkish}{loadhyph-tr.tex}{}{2}{2}
EOF
perl -pi -e 's|\\%%|%%|;' %{buildroot}%{_texmf_language_def_d}/hyphen-turkish
mkdir -p %{buildroot}%{_texmf_language_lua_d}
cat > %{buildroot}%{_texmf_language_lua_d}/hyphen-turkish <<EOF
-- from hyphen-turkish:
	['turkish'] = {
		loader = 'loadhyph-tr.tex',
		lefthyphenmin = 2,
		righthyphenmin = 2,
		synonyms = {  },
		patterns = 'hyph-tr.pat.txt',
		hyphenation = '',
	},
EOF


%changelog
* Tue Jan 24 2012 Paulo Andrade <pcpa@mandriva.com.br> 20110223-3
+ Revision: 767631
- Add workaround to rpm bug that broke hyphenation files
- Add workaround to rpm bug that broke hyphenation files

* Wed Jan 11 2012 Paulo Andrade <pcpa@mandriva.com.br> 20110223-2
+ Revision: 759941
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20110223-1
+ Revision: 718683
- texlive-hyphen-turkish
- texlive-hyphen-turkish
- texlive-hyphen-turkish
- texlive-hyphen-turkish

