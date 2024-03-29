# TODO
# - everything
%define		subver	37025
Summary:	Search and navigate IT data
Name:		splunk
Version:	3.2.4
Release:	0.3
License:	2005-2008 Splunk Inc
Group:		Applications
Source0:	http://download.splunk.com/releases/%{version}/linux/%{name}-%{version}-%{subver}-Linux-i686.tgz
# NoSource0-md5:	fd7beed52a2d6047cf781e75f49fd1f5
NoSource:	0
Source1:	http://download.splunk.com/releases/%{version}/linux/%{name}-%{version}-%{subver}-Linux-x86_64.tgz
# NoSource1-md5:	ad8a078b8a5a45ff5efa4559d7a45a09
NoSource:	1
URL:		http://www.splunk.com/
BuildRequires:	rpmbuild(macros) >= 1.202
Requires(postun):	/usr/sbin/groupdel
Requires(postun):	/usr/sbin/userdel
Requires(pre):	/bin/id
Requires(pre):	/usr/bin/getgid
Requires(pre):	/usr/sbin/groupadd
Requires(pre):	/usr/sbin/useradd
Requires:	bzip2
Requires:	bzip2-libs
Requires:	expat >= 1:2.0.0
Requires:	libarchive >= 2.0
Requires:	libxml2 >= 2.6.31
Requires:	libxslt
Requires:	pcre >= 7.6
Requires:	pcregrep
Requires:	pcretest
Requires:	zlib
#-PyXML-0.8.4.txt
#-Twisted-2.1.0.txt
#-TwistedWeb-0.5.0.txt
#-ZopeInterface-3.0.1.txt
#-expat-2.0.0.txt
#-fpconst-0.7.2.txt
#-gadflyZip.txt
#-httplib2-0.4.0.txt
#-libarchive-2.2.5.txt
#-libxml2-2.6.31.txt
#-libxslt-1.1.22.txt
#-log4py-1.3.txt
#-lxml-1.3.6.txt
#-lxml-elementtree-1.3.6.txt
#-openldap-2.3.27.txt
#-openssl-0.9.8g.txt
#-pcre-7.6.txt
#-xmlwrapp-0.5.0.txt
#pyOpenSSL-0.6.tar.gz
Provides:	group(splunk)
Provides:	user(splunk)
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir		%{_libdir}/%{name}

%description
Splunk is the search engine for IT data.

Splunk can index any data for which it has read access. If you don't
give it sufficient privileges, you may not be able to search all log
files, network ports or database tables.

%prep
%ifarch %{ix86}
%setup -q -T -n %{name} -b0
%endif
%ifarch %{x8664}
%setup -q -T -n %{name} -b1
%endif

rm -f .ftr

mv etc/splunk-launch.conf{.default,}

# zlib
%{__rm} lib/libz.so*

# bzip2
%{__rm} bin/{bunzip2,bzcat,bzcmp,bzdiff,bzegrep,bzfgrep,bzgrep,bzip2,bzip2recover,bzless,bzmore}
%{__rm} lib/libbz2.so*

# pcre
%{__rm} bin/{pcretest,pcregrep}
%{__rm} lib/libpcre.so*
%{__rm} lib/libpcreposix.so*

# libarchive
%{__rm} lib/libarchive.so*

# expat
%{__rm} lib/libexpat.so*

# libxslt
%{__rm} lib/libexslt.so*
%{__rm} lib/libxslt.so*

# libxml2
%{__rm} lib/libxml2.so*

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_includedir},%{_appdir}}
cp -a bin etc lib openssl share $RPM_BUILD_ROOT%{_appdir}
cp -a include/*.h $RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%pre
%groupadd -g 230 splunk
%useradd -u 230 -d %{_appdir} -g splunk -c "Splunk User" splunk

%postun
if [ "$1" = "0" ]; then
	%userremove splunk
	%groupremove splunk
fi

%files
%defattr(644,root,root,755)
%doc README.txt license.txt
%dir %attr(555,splunk,splunk) %{_appdir}
%dir %attr(555,splunk,splunk) %{_appdir}/bin
%attr(555,splunk,splunk) %{_appdir}/bin/btool
%attr(555,splunk,splunk) %{_appdir}/bin/classify
%attr(755,splunk,splunk) %{_appdir}/bin/compressedExport.sh
%attr(555,splunk,splunk) %{_appdir}/bin/dbmanipulator.py
%attr(444,splunk,splunk) %{_appdir}/bin/dictionary.txt
%attr(555,splunk,splunk) %{_appdir}/bin/exporttool
%attr(555,splunk,splunk) %{_appdir}/bin/fix-hashdb-lic
%attr(755,splunk,splunk) %{_appdir}/bin/flatfileExport.sh
%attr(555,splunk,splunk) %{_appdir}/bin/genAuditKeys.py
%attr(555,splunk,splunk) %{_appdir}/bin/genRootCA.sh
%attr(555,splunk,splunk) %{_appdir}/bin/genSignedServerCert.py
%attr(555,splunk,splunk) %{_appdir}/bin/genSignedServerCert.sh
%attr(555,splunk,splunk) %{_appdir}/bin/genWebCert.py
%attr(555,splunk,splunk) %{_appdir}/bin/genWebCert.sh
%attr(555,splunk,splunk) %{_appdir}/bin/gzdumper
%attr(555,splunk,splunk) %{_appdir}/bin/listtails
%attr(555,splunk,splunk) %{_appdir}/bin/locktest
%attr(555,splunk,splunk) %{_appdir}/bin/locktool
%attr(555,splunk,splunk) %{_appdir}/bin/migrate_2x_data_to_3x.py
%attr(555,splunk,splunk) %{_appdir}/bin/migrate_2x_exported_data_to_3x.py
%attr(555,splunk,splunk) %{_appdir}/bin/migratehashdb
%attr(555,splunk,splunk) %{_appdir}/bin/minigzip
%attr(444,splunk,splunk) %{_appdir}/bin/names.txt
%attr(555,splunk,splunk) %{_appdir}/bin/openssl
%attr(555,splunk,splunk) %{_appdir}/bin/parsetest
%attr(555,splunk,splunk) %{_appdir}/bin/pcregextest
%attr(444,splunk,splunk) %{_appdir}/bin/private-terms.txt
%attr(444,splunk,splunk) %{_appdir}/bin/public-terms.txt
%attr(555,splunk,splunk) %{_appdir}/bin/python
%attr(555,splunk,splunk) %{_appdir}/bin/python2.5
%attr(555,splunk,splunk) %{_appdir}/bin/regextest
%attr(555,splunk,splunk) %{_appdir}/bin/rest_handler.py
%attr(555,splunk,splunk) %{_appdir}/bin/resurrectionJoe
%dir %attr(555,splunk,splunk) %{_appdir}/bin/scripts
%attr(444,splunk,splunk) %{_appdir}/bin/scripts/readme.txt
%attr(555,splunk,splunk) %{_appdir}/bin/scrubber.py
%attr(555,splunk,splunk) %{_appdir}/bin/searchtest
%attr(555,splunk,splunk) %{_appdir}/bin/seedFileTyper.py
%attr(444,splunk,splunk) %{_appdir}/bin/setSplunkEnv
%attr(555,splunk,splunk) %{_appdir}/bin/signtool
%attr(555,splunk,splunk) %{_appdir}/bin/splunk
%attr(555,splunk,splunk) %{_appdir}/bin/splunk-optimize
%attr(555,splunk,splunk) %{_appdir}/bin/splunkd
%attr(555,splunk,splunk) %{_appdir}/bin/splunkexport.py
%attr(555,splunk,splunk) %{_appdir}/bin/splunkimport.py
%attr(555,splunk,splunk) %{_appdir}/bin/splunkmon
%attr(555,splunk,splunk) %{_appdir}/bin/sqlite3
%attr(555,splunk,splunk) %{_appdir}/bin/tarit.py
%attr(555,splunk,splunk) %{_appdir}/bin/tocsv.py
%attr(555,splunk,splunk) %{_appdir}/bin/tsidxprobe
%attr(444,splunk,splunk) %{_appdir}/bin/twistd
%attr(444,splunk,splunk) %{_appdir}/bin/xmlproc_parse
%attr(555,splunk,splunk) %{_appdir}/bin/xmlwf
%attr(555,splunk,splunk) %{_appdir}/bin/xr5
%dir %attr(755,splunk,splunk) %{_appdir}/etc
%attr(644,splunk,splunk) %{_appdir}/etc/SplunkWeb.tac
%dir %attr(755,splunk,splunk) %{_appdir}/etc/auth
%attr(444,splunk,splunk) %{_appdir}/etc/auth/ca.pem
%attr(444,splunk,splunk) %{_appdir}/etc/auth/cacert.pem
%attr(444,splunk,splunk) %{_appdir}/etc/authRolesAndTypes.xml
%dir %attr(755,splunk,splunk) %{_appdir}/etc/bundles
%dir %attr(555,splunk,splunk) %{_appdir}/etc/bundles/README
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/README/alert_actions.conf.example
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/README/alert_actions.conf.spec
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/README/audit.conf.example
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/README/audit.conf.spec
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/README/authentication.conf.example
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/README/authentication.conf.spec
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/README/authorize.conf.example
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/README/authorize.conf.spec
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/README/decorations.conf.example
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/README/decorations.conf.spec
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/README/deployment.conf.example
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/README/deployment.conf.spec
%dir %attr(555,splunk,splunk) %{_appdir}/etc/bundles/README/deprecated
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/README/deprecated/access_controls.conf.example
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/README/deprecated/access_controls.conf.spec
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/README/deprecated/metaevents.conf.example
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/README/deprecated/metaevents.conf.spec
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/README/distsearch.conf.example
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/README/distsearch.conf.spec
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/README/eventdiscoverer.conf.example
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/README/eventdiscoverer.conf.spec
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/README/eventtypes.conf.example
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/README/eventtypes.conf.spec
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/README/field_actions.conf.example
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/README/field_actions.conf.spec
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/README/fields.conf.example
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/README/fields.conf.spec
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/README/indexes.conf.example
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/README/indexes.conf.spec
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/README/inputs.conf.example
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/README/inputs.conf.spec
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/README/limits.conf.example
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/README/limits.conf.spec
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/README/literals.conf.example
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/README/literals.conf.spec
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/README/multikv.conf.example
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/README/multikv.conf.spec
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/README/outputs.conf.example
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/README/outputs.conf.spec
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/README/prefs.conf.example
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/README/prefs.conf.spec
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/README/props.conf.example
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/README/props.conf.spec
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/README/restmap.conf.example
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/README/restmap.conf.spec
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/README/savedsearches.conf.example
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/README/savedsearches.conf.spec
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/README/segmenters.conf.example
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/README/segmenters.conf.spec
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/README/server.conf.example
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/README/server.conf.spec
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/README/source-classifier.conf.example
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/README/source-classifier.spec
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/README/sourcetypes.conf.example
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/README/sourcetypes.conf.spec
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/README/streams.conf.example
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/README/streams.conf.spec
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/README/transactiontypes.conf.example
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/README/transactiontypes.conf.spec
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/README/transforms.conf.example
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/README/transforms.conf.spec
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/README/user-seed.conf.example
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/README/user-seed.conf.spec
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/README/web.conf.example
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/README/web.conf.spec
%dir %attr(555,splunk,splunk) %{_appdir}/etc/bundles/code
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/code/props.conf
%dir %attr(555,splunk,splunk) %{_appdir}/etc/bundles/config
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/config/props.conf
%dir %attr(555,splunk,splunk) %{_appdir}/etc/bundles/debug
%dir %attr(555,splunk,splunk) %{_appdir}/etc/bundles/debug/rest
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/debug/rest/debugutils.py
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/debug/restmap.conf
%dir %attr(755,splunk,splunk) %{_appdir}/etc/bundles/default
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/default/alert_actions.conf
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/default/api.conf
%attr(600,splunk,splunk) %{_appdir}/etc/bundles/default/authentication.conf
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/default/authorize.conf
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/default/decorations.conf
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/default/eventdiscoverer.conf
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/default/eventtypes.conf
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/default/field_actions.conf
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/default/fields.conf
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/default/indexes.conf
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/default/inputs.conf
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/default/limits.conf
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/default/literals.conf
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/default/metaevents.conf
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/default/prefs.conf
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/default/props.conf
%dir %attr(555,splunk,splunk) %{_appdir}/etc/bundles/default/rest
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/default/rest/defaultadmin.py
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/default/restmap.conf
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/default/savedsearches.conf
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/default/segmenters.conf
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/default/server.conf
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/default/source-classifier.conf
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/default/sourcetypes.conf
%dir %attr(555,splunk,splunk) %{_appdir}/etc/bundles/default/spec
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/default/spec/alert_actions.spec
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/default/spec/audit.spec
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/default/spec/authorize.spec
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/default/spec/default.spec
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/default/spec/deployment.spec
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/default/spec/distsearch.spec
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/default/spec/eventdiscoverer.spec
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/default/spec/eventtypes.spec
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/default/spec/field_actions.spec
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/default/spec/indexes.spec
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/default/spec/inputs.spec
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/default/spec/limits.spec
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/default/spec/metaevents.spec
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/default/spec/outputs.spec
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/default/spec/prefs.spec
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/default/spec/props.spec
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/default/spec/savedsearches.spec
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/default/spec/segmenters.spec
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/default/spec/server.spec
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/default/spec/source-classifier.spec
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/default/spec/spec.dtd
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/default/spec/transforms.spec
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/default/spec/web.spec
%dir %attr(555,splunk,splunk) %{_appdir}/etc/bundles/default/static
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/default/static/atom.xsl
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/default/streams.conf
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/default/strings.conf
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/default/transactiontypes.conf
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/default/transforms.conf
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/default/user-seed.conf
%dir %attr(555,splunk,splunk) %{_appdir}/etc/bundles/default/web
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/default/web.conf
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/default/web/FieldLearning.py
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/default/web/addeventtype.html
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/default/web/addeventtype.py
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/default/web/addeventtype_done.html
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/default/web/fields.py
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/default/web/learn.html
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/default/web/surrounding_events.py
%dir %attr(755,splunk,splunk) %{_appdir}/etc/bundles/learned
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/learned/README
%dir %attr(755,splunk,splunk) %{_appdir}/etc/bundles/local
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/local/README
%dir %attr(555,splunk,splunk) %{_appdir}/etc/bundles/samples
%dir %attr(555,splunk,splunk) %{_appdir}/etc/bundles/samples/bin
%attr(555,splunk,splunk) %{_appdir}/etc/bundles/samples/bin/eatsamples.py
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/samples/eventdiscoverer.conf
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/samples/indexes.conf
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/samples/inputs.conf
%dir %attr(555,splunk,splunk) %{_appdir}/etc/bundles/samples/logs
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/samples/logs/access.combined.log.sample
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/samples/logs/apache.error.log.sample
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/samples/logs/db2diag.log.sample
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/samples/logs/http1access.log.sample
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/samples/logs/http2access.log.sample
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/samples/logs/syslogsample.log.sample
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/samples/logs/was1activity.txt.sample
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/samples/logs/was2activity.txt.sample
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/samples/logs/websphere.trlog.syserr.log.sample
%dir %attr(555,splunk,splunk) %{_appdir}/etc/bundles/samples/rest
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/samples/rest/samplehandlers.py
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/samples/restmap.conf
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/samples/savedsearches.conf
%dir %attr(555,splunk,splunk) %{_appdir}/etc/bundles/text
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/text/props.conf
%dir %attr(555,splunk,splunk) %{_appdir}/etc/bundles/web
%attr(444,splunk,splunk) %{_appdir}/etc/bundles/web/props.conf
%attr(444,splunk,splunk) %{_appdir}/etc/datetime.xml
%dir %attr(755,splunk,splunk) %{_appdir}/etc/disabled-bundles
%attr(444,splunk,splunk) %{_appdir}/etc/disabled-bundles/README
%attr(644,splunk,splunk) %{_appdir}/etc/findlogs.ini
%dir %attr(555,splunk,splunk) %{_appdir}/etc/init.d
%attr(444,splunk,splunk) %{_appdir}/etc/init.d/README
%attr(444,splunk,splunk) %{_appdir}/etc/log-cmdline.cfg
%attr(444,splunk,splunk) %{_appdir}/etc/log-debug.cfg
%attr(644,splunk,splunk) %{_appdir}/etc/log.cfg
%dir %attr(555,splunk,splunk) %{_appdir}/etc/modules
%dir %attr(555,splunk,splunk) %{_appdir}/etc/modules/distributedDeployment
%attr(444,splunk,splunk) %{_appdir}/etc/modules/distributedDeployment/config.xml
%dir %attr(555,splunk,splunk) %{_appdir}/etc/modules/distributedDeploymentClient
%attr(444,splunk,splunk) %{_appdir}/etc/modules/distributedDeploymentClient/config.xml
%dir %attr(755,splunk,splunk) %{_appdir}/etc/modules/distributedSearch
%attr(644,splunk,splunk) %{_appdir}/etc/modules/distributedSearch/config.xml.default
%dir %attr(555,splunk,splunk) %{_appdir}/etc/modules/input
%dir %attr(555,splunk,splunk) %{_appdir}/etc/modules/input/FIFO
%attr(444,splunk,splunk) %{_appdir}/etc/modules/input/FIFO/config.xml
%dir %attr(555,splunk,splunk) %{_appdir}/etc/modules/input/TCP
%attr(444,splunk,splunk) %{_appdir}/etc/modules/input/TCP/config.xml
%dir %attr(555,splunk,splunk) %{_appdir}/etc/modules/input/UDP
%attr(444,splunk,splunk) %{_appdir}/etc/modules/input/UDP/config.xml
%dir %attr(555,splunk,splunk) %{_appdir}/etc/modules/input/exec
%attr(444,splunk,splunk) %{_appdir}/etc/modules/input/exec/config.xml
%dir %attr(555,splunk,splunk) %{_appdir}/etc/modules/input/fschangemanager
%attr(444,splunk,splunk) %{_appdir}/etc/modules/input/fschangemanager/config.xml
%dir %attr(555,splunk,splunk) %{_appdir}/etc/modules/input/log4jTCP
%attr(444,splunk,splunk) %{_appdir}/etc/modules/input/log4jTCP/config.xml.disabled
%dir %attr(555,splunk,splunk) %{_appdir}/etc/modules/input/splunkTCP
%attr(444,splunk,splunk) %{_appdir}/etc/modules/input/splunkTCP/config.xml.disabled
%dir %attr(555,splunk,splunk) %{_appdir}/etc/modules/input/syslogFIFO
%attr(444,splunk,splunk) %{_appdir}/etc/modules/input/syslogFIFO/config.xml.disabled
%dir %attr(555,splunk,splunk) %{_appdir}/etc/modules/input/syslogUDP
%attr(444,splunk,splunk) %{_appdir}/etc/modules/input/syslogUDP/config.xml.disabled
%dir %attr(555,splunk,splunk) %{_appdir}/etc/modules/input/tailfile
%attr(444,splunk,splunk) %{_appdir}/etc/modules/input/tailfile/config.xml
%dir %attr(555,splunk,splunk) %{_appdir}/etc/modules/internal
%dir %attr(555,splunk,splunk) %{_appdir}/etc/modules/internal/scheduler
%attr(444,splunk,splunk) %{_appdir}/etc/modules/internal/scheduler/config.xml
%dir %attr(555,splunk,splunk) %{_appdir}/etc/modules/parsing
%attr(444,splunk,splunk) %{_appdir}/etc/modules/parsing/config.xml
%attr(444,splunk,splunk) %{_appdir}/etc/modules/parsing/config.xml-oxiclean
%dir %attr(755,splunk,splunk) %{_appdir}/etc/myinstall
%dir %attr(555,splunk,splunk) %{_appdir}/etc/myinstall/pluginConfs
%attr(444,splunk,splunk) %{_appdir}/etc/myinstall/pluginConfs/cleaners.xml
%attr(444,splunk,splunk) %{_appdir}/etc/myinstall/pluginConfs/emptyConfig.xml
%attr(444,splunk,splunk) %{_appdir}/etc/myinstall/pluginConfs/majorOnly_cleaners.xml
%attr(444,splunk,splunk) %{_appdir}/etc/myinstall/pluginConfs/splunklogger_cleaners.xml
%attr(644,splunk,splunk) %{_appdir}/etc/myinstall/splunkd.xml.default
%attr(644,splunk,splunk) %{_appdir}/etc/myinstall/splunkd.xml.forwarder
%attr(444,splunk,splunk) %{_appdir}/etc/myinstall/users.xml
%dir %attr(555,splunk,splunk) %{_appdir}/etc/ngram-models
%attr(444,splunk,splunk) %{_appdir}/etc/ngram-models/_afrikaans.ngrams
%attr(444,splunk,splunk) %{_appdir}/etc/ngram-models/_albanian.ngrams
%attr(444,splunk,splunk) %{_appdir}/etc/ngram-models/_amharic-UTF-8.ngrams
%attr(444,splunk,splunk) %{_appdir}/etc/ngram-models/_arabic-CP1256.ngrams
%attr(444,splunk,splunk) %{_appdir}/etc/ngram-models/_arabic-ISO-8859-6.ngrams
%attr(444,splunk,splunk) %{_appdir}/etc/ngram-models/_armenian-ARMSCII-8.ngrams
%attr(444,splunk,splunk) %{_appdir}/etc/ngram-models/_basque.ngrams
%attr(444,splunk,splunk) %{_appdir}/etc/ngram-models/_belarus-CP1251.ngrams
%attr(444,splunk,splunk) %{_appdir}/etc/ngram-models/_bosnian.ngrams
%attr(444,splunk,splunk) %{_appdir}/etc/ngram-models/_breton.ngrams
%attr(444,splunk,splunk) %{_appdir}/etc/ngram-models/_bulgarian-ISO-8859-5.ngrams
%attr(444,splunk,splunk) %{_appdir}/etc/ngram-models/_catalan.ngrams
%attr(444,splunk,splunk) %{_appdir}/etc/ngram-models/_chinese-BIG5.ngrams
%attr(444,splunk,splunk) %{_appdir}/etc/ngram-models/_chinese-GB2312.ngrams
%attr(444,splunk,splunk) %{_appdir}/etc/ngram-models/_croatian-ASCII.ngrams
%attr(444,splunk,splunk) %{_appdir}/etc/ngram-models/_czech-ISO-8859-2.ngrams
%attr(444,splunk,splunk) %{_appdir}/etc/ngram-models/_danish.ngrams
%attr(444,splunk,splunk) %{_appdir}/etc/ngram-models/_dutch.ngrams
%attr(444,splunk,splunk) %{_appdir}/etc/ngram-models/_english.ngrams
%attr(444,splunk,splunk) %{_appdir}/etc/ngram-models/_esperanto.ngrams
%attr(444,splunk,splunk) %{_appdir}/etc/ngram-models/_estonian.ngrams
%attr(444,splunk,splunk) %{_appdir}/etc/ngram-models/_finnish.ngrams
%attr(444,splunk,splunk) %{_appdir}/etc/ngram-models/_french.ngrams
%attr(444,splunk,splunk) %{_appdir}/etc/ngram-models/_frisian.ngrams
%attr(444,splunk,splunk) %{_appdir}/etc/ngram-models/_georgian-Georgian-Academy.ngrams
%attr(444,splunk,splunk) %{_appdir}/etc/ngram-models/_german.ngrams
%attr(444,splunk,splunk) %{_appdir}/etc/ngram-models/_greek-ISO-8859-7.ngrams
%attr(444,splunk,splunk) %{_appdir}/etc/ngram-models/_hawaian.ngrams
%attr(444,splunk,splunk) %{_appdir}/etc/ngram-models/_hebrew-ISO-8859-8.ngrams
%attr(444,splunk,splunk) %{_appdir}/etc/ngram-models/_hindi.ngrams
%attr(444,splunk,splunk) %{_appdir}/etc/ngram-models/_hungarian.ngrams
%attr(444,splunk,splunk) %{_appdir}/etc/ngram-models/_icelandic.ngrams
%attr(444,splunk,splunk) %{_appdir}/etc/ngram-models/_indonesian.ngrams
%attr(444,splunk,splunk) %{_appdir}/etc/ngram-models/_irish.ngrams
%attr(444,splunk,splunk) %{_appdir}/etc/ngram-models/_italian.ngrams
%attr(444,splunk,splunk) %{_appdir}/etc/ngram-models/_japanese-EUC-JP.ngrams
%attr(444,splunk,splunk) %{_appdir}/etc/ngram-models/_japanese-SHIFT-JIS.ngrams
%attr(444,splunk,splunk) %{_appdir}/etc/ngram-models/_korean-EUC-KR.ngrams
%attr(444,splunk,splunk) %{_appdir}/etc/ngram-models/_latin.ngrams
%attr(444,splunk,splunk) %{_appdir}/etc/ngram-models/_latvian.ngrams
%attr(444,splunk,splunk) %{_appdir}/etc/ngram-models/_lithuanian.ngrams
%attr(444,splunk,splunk) %{_appdir}/etc/ngram-models/_malay.ngrams
%attr(444,splunk,splunk) %{_appdir}/etc/ngram-models/_manx.ngrams
%attr(444,splunk,splunk) %{_appdir}/etc/ngram-models/_marathi.ngrams
%attr(444,splunk,splunk) %{_appdir}/etc/ngram-models/_mf.ngrams
%attr(444,splunk,splunk) %{_appdir}/etc/ngram-models/_middle_frisian.ngrams
%attr(444,splunk,splunk) %{_appdir}/etc/ngram-models/_mingo.ngrams
%attr(444,splunk,splunk) %{_appdir}/etc/ngram-models/_nepali.ngrams
%attr(444,splunk,splunk) %{_appdir}/etc/ngram-models/_norwegian.ngrams
%attr(444,splunk,splunk) %{_appdir}/etc/ngram-models/_persian.ngrams
%attr(444,splunk,splunk) %{_appdir}/etc/ngram-models/_polish.ngrams
%attr(444,splunk,splunk) %{_appdir}/etc/ngram-models/_portuguese.ngrams
%attr(444,splunk,splunk) %{_appdir}/etc/ngram-models/_quechua.ngrams
%attr(444,splunk,splunk) %{_appdir}/etc/ngram-models/_romanian.ngrams
%attr(444,splunk,splunk) %{_appdir}/etc/ngram-models/_rumantsch.ngrams
%attr(444,splunk,splunk) %{_appdir}/etc/ngram-models/_russian-CP1251.ngrams
%attr(444,splunk,splunk) %{_appdir}/etc/ngram-models/_russian-ISO-8859-5.ngrams
%attr(444,splunk,splunk) %{_appdir}/etc/ngram-models/_russian-KOI8-R.ngrams
%attr(444,splunk,splunk) %{_appdir}/etc/ngram-models/_sanskrit.ngrams
%attr(444,splunk,splunk) %{_appdir}/etc/ngram-models/_scots.ngrams
%attr(444,splunk,splunk) %{_appdir}/etc/ngram-models/_scots_gaelic.ngrams
%attr(444,splunk,splunk) %{_appdir}/etc/ngram-models/_serbian-ASCII.ngrams
%attr(444,splunk,splunk) %{_appdir}/etc/ngram-models/_slovak-ASCII.ngrams
%attr(444,splunk,splunk) %{_appdir}/etc/ngram-models/_slovak-CP1250.ngrams
%attr(444,splunk,splunk) %{_appdir}/etc/ngram-models/_slovenian-ASCII.ngrams
%attr(444,splunk,splunk) %{_appdir}/etc/ngram-models/_slovenian-ISO-8859-2.ngrams
%attr(444,splunk,splunk) %{_appdir}/etc/ngram-models/_spanish.ngrams
%attr(444,splunk,splunk) %{_appdir}/etc/ngram-models/_swahili.ngrams
%attr(444,splunk,splunk) %{_appdir}/etc/ngram-models/_swedish.ngrams
%attr(444,splunk,splunk) %{_appdir}/etc/ngram-models/_tagalog.ngrams
%attr(444,splunk,splunk) %{_appdir}/etc/ngram-models/_tamil.ngrams
%attr(444,splunk,splunk) %{_appdir}/etc/ngram-models/_thai-TIS-620.ngrams
%attr(444,splunk,splunk) %{_appdir}/etc/ngram-models/_turkish.ngrams
%attr(444,splunk,splunk) %{_appdir}/etc/ngram-models/_ukrainian-KOI8-U.ngrams
%attr(444,splunk,splunk) %{_appdir}/etc/ngram-models/_vietnamese-VISCII.ngrams
%attr(444,splunk,splunk) %{_appdir}/etc/ngram-models/_welsh.ngrams
%attr(444,splunk,splunk) %{_appdir}/etc/ngram-models/_yiddish-UTF-8.ngrams
%dir %attr(555,splunk,splunk) %{_appdir}/etc/openldap
%attr(444,splunk,splunk) %{_appdir}/etc/openldap/ldap.conf
%attr(444,splunk,splunk) %{_appdir}/etc/prettyprint.xsl
%attr(444,splunk,splunk) %{_appdir}/etc/properties.xml
%attr(444,splunk,splunk) %{_appdir}/etc/searchLanguage.xml
%dir %attr(755,splunk,splunk) %{_appdir}/etc/searchscripts
%attr(555,splunk,splunk) %{_appdir}/etc/searchscripts/createrss.py
%attr(555,splunk,splunk) %{_appdir}/etc/searchscripts/diff.py
%attr(555,splunk,splunk) %{_appdir}/etc/searchscripts/gentimes.py
%attr(555,splunk,splunk) %{_appdir}/etc/searchscripts/head.py
%attr(555,splunk,splunk) %{_appdir}/etc/searchscripts/idxprobe.py
%attr(555,splunk,splunk) %{_appdir}/etc/searchscripts/iplocation.py
%attr(555,splunk,splunk) %{_appdir}/etc/searchscripts/marklar.py
%attr(555,splunk,splunk) %{_appdir}/etc/searchscripts/runshellscript.py
%attr(555,splunk,splunk) %{_appdir}/etc/searchscripts/sendemail.py
%attr(644,splunk,splunk) %{_appdir}/etc/searchscripts/translate.conf
%attr(555,splunk,splunk) %{_appdir}/etc/searchscripts/translate.py
%attr(555,splunk,splunk) %{_appdir}/etc/searchscripts/transpose.py
%attr(555,splunk,splunk) %{_appdir}/etc/searchscripts/uniq.py
%attr(555,splunk,splunk) %{_appdir}/etc/searchscripts/windbag.py
%attr(555,splunk,splunk) %{_appdir}/etc/searchscripts/xmlkv.py
%attr(555,splunk,splunk) %{_appdir}/etc/searchscripts/xmlunescape.py
%attr(644,splunk,splunk) %{_appdir}/etc/splunk-free.license
%config(noreplace) %verify(not md5 mtime size) %{_appdir}/etc/splunk-launch.conf
%attr(444,splunk,splunk) %{_appdir}/etc/splunk.version

# -devel
%{_includedir}/splunk-extplugin.h

%dir %attr(555,splunk,splunk) %{_appdir}/lib
%dir %attr(555,splunk,splunk) %{_appdir}/lib/engines
%attr(555,splunk,splunk) %{_appdir}/lib/engines/lib4758cca.so
%attr(555,splunk,splunk) %{_appdir}/lib/engines/libaep.so
%attr(555,splunk,splunk) %{_appdir}/lib/engines/libatalla.so
%attr(555,splunk,splunk) %{_appdir}/lib/engines/libchil.so
%attr(555,splunk,splunk) %{_appdir}/lib/engines/libcswift.so
%attr(555,splunk,splunk) %{_appdir}/lib/engines/libgmp.so
%attr(555,splunk,splunk) %{_appdir}/lib/engines/libnuron.so
%attr(555,splunk,splunk) %{_appdir}/lib/engines/libsureware.so
%attr(555,splunk,splunk) %{_appdir}/lib/engines/libubsec.so
%attr(555,splunk,splunk) %{_appdir}/lib/libcrypto.so
%attr(555,splunk,splunk) %{_appdir}/lib/libcrypto.so.0.9.8
%attr(555,splunk,splunk) %{_appdir}/lib/libextcmdapi.so
%attr(555,splunk,splunk) %{_appdir}/lib/libextcmdapi.so.0
%attr(555,splunk,splunk) %{_appdir}/lib/libextcmdapi.so.0.0.0
%attr(555,splunk,splunk) %{_appdir}/lib/libsqlite3.so
%attr(555,splunk,splunk) %{_appdir}/lib/libsqlite3.so.0
%attr(555,splunk,splunk) %{_appdir}/lib/libsqlite3.so.0.8.6
%attr(555,splunk,splunk) %{_appdir}/lib/libssl.so
%attr(555,splunk,splunk) %{_appdir}/lib/libssl.so.0.9.8

%dir %attr(555,splunk,splunk) %{_appdir}/lib/python2.5
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/BaseHTTPServer.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/Bastion.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/CGIHTTPServer.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/ConfigParser.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/Cookie.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/DocXMLRPCServer.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/HTMLParser.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/LICENSE.txt
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/MimeWriter.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/Queue.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/SimpleHTTPServer.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/SimpleXMLRPCServer.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/SocketServer.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/StringIO.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/UserDict.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/UserList.py
%attr(555,splunk,splunk) %{_appdir}/lib/python2.5/UserString.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/_LWPCookieJar.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/_MozillaCookieJar.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/__future__.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/__phello__.foo.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/_strptime.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/_threading_local.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/aifc.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/anydbm.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/asynchat.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/asyncore.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/atexit.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/audiodev.py
%attr(555,splunk,splunk) %{_appdir}/lib/python2.5/base64.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/bdb.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/binhex.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/bisect.py
%attr(555,splunk,splunk) %{_appdir}/lib/python2.5/cProfile.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/calendar.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/cgi.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/cgitb.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/chunk.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/cmd.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/code.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/codecs.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/codeop.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/colorsys.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/commands.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/compileall.py
%dir %attr(555,splunk,splunk) %{_appdir}/lib/python2.5/compiler
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/compiler/__init__.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/compiler/ast.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/compiler/consts.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/compiler/future.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/compiler/misc.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/compiler/pyassem.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/compiler/pycodegen.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/compiler/symbols.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/compiler/syntax.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/compiler/transformer.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/compiler/visitor.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/contextlib.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/cookielib.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/copy.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/copy_reg.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/csv.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/dbhash.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/decimal.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/difflib.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/dircache.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/dis.py
%dir %attr(555,splunk,splunk) %{_appdir}/lib/python2.5/distutils
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/distutils/README
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/distutils/__init__.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/distutils/archive_util.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/distutils/bcppcompiler.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/distutils/ccompiler.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/distutils/cmd.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/distutils/core.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/distutils/cygwinccompiler.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/distutils/debug.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/distutils/dep_util.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/distutils/dir_util.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/distutils/dist.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/distutils/emxccompiler.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/distutils/errors.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/distutils/extension.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/distutils/fancy_getopt.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/distutils/file_util.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/distutils/filelist.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/distutils/log.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/distutils/msvccompiler.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/distutils/mwerkscompiler.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/distutils/spawn.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/distutils/sysconfig.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/distutils/text_file.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/distutils/unixccompiler.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/distutils/util.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/distutils/version.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/distutils/versionpredicate.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/doctest.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/dumbdbm.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/dummy_thread.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/dummy_threading.py
%dir %attr(555,splunk,splunk) %{_appdir}/lib/python2.5/email
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/email/__init__.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/email/_parseaddr.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/email/base64mime.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/email/charset.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/email/encoders.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/email/errors.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/email/feedparser.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/email/generator.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/email/header.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/email/iterators.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/email/message.py
%dir %attr(555,splunk,splunk) %{_appdir}/lib/python2.5/email/mime
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/email/mime/__init__.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/email/mime/application.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/email/mime/audio.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/email/mime/base.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/email/mime/image.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/email/mime/message.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/email/mime/multipart.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/email/mime/nonmultipart.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/email/mime/text.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/email/parser.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/email/quoprimime.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/email/utils.py
%dir %attr(555,splunk,splunk) %{_appdir}/lib/python2.5/encodings
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/__init__.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/aliases.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/ascii.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/base64_codec.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/big5.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/big5hkscs.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/bz2_codec.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/charmap.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/cp037.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/cp1006.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/cp1026.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/cp1140.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/cp1250.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/cp1251.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/cp1252.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/cp1253.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/cp1254.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/cp1255.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/cp1256.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/cp1257.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/cp1258.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/cp424.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/cp437.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/cp500.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/cp737.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/cp775.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/cp850.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/cp852.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/cp855.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/cp856.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/cp857.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/cp860.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/cp861.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/cp862.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/cp863.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/cp864.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/cp865.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/cp866.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/cp869.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/cp874.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/cp875.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/cp932.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/cp949.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/cp950.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/euc_jis_2004.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/euc_jisx0213.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/euc_jp.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/euc_kr.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/gb18030.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/gb2312.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/gbk.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/hex_codec.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/hp_roman8.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/hz.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/idna.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/iso2022_jp.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/iso2022_jp_1.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/iso2022_jp_2.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/iso2022_jp_2004.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/iso2022_jp_3.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/iso2022_jp_ext.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/iso2022_kr.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/iso8859_1.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/iso8859_10.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/iso8859_11.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/iso8859_13.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/iso8859_14.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/iso8859_15.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/iso8859_16.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/iso8859_2.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/iso8859_3.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/iso8859_4.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/iso8859_5.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/iso8859_6.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/iso8859_7.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/iso8859_8.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/iso8859_9.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/johab.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/koi8_r.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/koi8_u.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/latin_1.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/mac_arabic.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/mac_centeuro.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/mac_croatian.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/mac_cyrillic.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/mac_farsi.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/mac_greek.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/mac_iceland.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/mac_latin2.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/mac_roman.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/mac_romanian.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/mac_turkish.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/mbcs.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/palmos.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/ptcp154.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/punycode.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/quopri_codec.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/raw_unicode_escape.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/rot_13.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/shift_jis.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/shift_jis_2004.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/shift_jisx0213.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/string_escape.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/tis_620.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/undefined.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/unicode_escape.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/unicode_internal.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/utf_16.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/utf_16_be.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/utf_16_le.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/utf_7.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/utf_8.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/utf_8_sig.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/uu_codec.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/encodings/zlib_codec.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/filecmp.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/fileinput.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/fnmatch.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/formatter.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/fpformat.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/ftplib.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/functools.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/getopt.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/getpass.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/gettext.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/glob.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/gopherlib.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/gzip.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/hashlib.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/heapq.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/hmac.py
%dir %attr(555,splunk,splunk) %{_appdir}/lib/python2.5/hotshot
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/hotshot/__init__.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/hotshot/log.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/hotshot/stats.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/hotshot/stones.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/htmlentitydefs.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/htmllib.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/httplib.py
%dir %attr(555,splunk,splunk) %{_appdir}/lib/python2.5/idlelib
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/idlelib/AutoComplete.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/idlelib/AutoCompleteWindow.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/idlelib/AutoExpand.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/idlelib/Bindings.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/idlelib/CREDITS.txt
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/idlelib/CallTipWindow.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/idlelib/CallTips.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/idlelib/ChangeLog
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/idlelib/ClassBrowser.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/idlelib/CodeContext.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/idlelib/ColorDelegator.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/idlelib/Debugger.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/idlelib/Delegator.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/idlelib/EditorWindow.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/idlelib/FileList.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/idlelib/FormatParagraph.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/idlelib/GrepDialog.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/idlelib/HISTORY.txt
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/idlelib/HyperParser.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/idlelib/IOBinding.py
%dir %attr(555,splunk,splunk) %{_appdir}/lib/python2.5/idlelib/Icons
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/idlelib/Icons/folder.gif
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/idlelib/Icons/idle.icns
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/idlelib/Icons/minusnode.gif
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/idlelib/Icons/openfolder.gif
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/idlelib/Icons/plusnode.gif
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/idlelib/Icons/python.gif
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/idlelib/Icons/tk.gif
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/idlelib/IdleHistory.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/idlelib/MultiCall.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/idlelib/MultiStatusBar.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/idlelib/NEWS.txt
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/idlelib/ObjectBrowser.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/idlelib/OutputWindow.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/idlelib/ParenMatch.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/idlelib/PathBrowser.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/idlelib/Percolator.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/idlelib/PyParse.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/idlelib/PyShell.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/idlelib/README.txt
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/idlelib/RemoteDebugger.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/idlelib/RemoteObjectBrowser.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/idlelib/ReplaceDialog.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/idlelib/ScriptBinding.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/idlelib/ScrolledList.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/idlelib/SearchDialog.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/idlelib/SearchDialogBase.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/idlelib/SearchEngine.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/idlelib/StackViewer.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/idlelib/TODO.txt
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/idlelib/ToolTip.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/idlelib/TreeWidget.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/idlelib/UndoDelegator.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/idlelib/WidgetRedirector.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/idlelib/WindowList.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/idlelib/ZoomHeight.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/idlelib/__init__.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/idlelib/aboutDialog.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/idlelib/config-extensions.def
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/idlelib/config-highlight.def
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/idlelib/config-keys.def
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/idlelib/config-main.def
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/idlelib/configDialog.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/idlelib/configHandler.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/idlelib/configHelpSourceEdit.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/idlelib/configSectionNameDialog.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/idlelib/dynOptionMenuWidget.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/idlelib/extend.txt
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/idlelib/help.txt
%attr(555,splunk,splunk) %{_appdir}/lib/python2.5/idlelib/idle.bat
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/idlelib/idle.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/idlelib/idle.pyw
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/idlelib/idlever.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/idlelib/keybindingDialog.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/idlelib/macosxSupport.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/idlelib/rpc.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/idlelib/run.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/idlelib/tabpage.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/idlelib/testcode.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/idlelib/textView.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/ihooks.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/imaplib.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/imghdr.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/imputil.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/inspect.py
%attr(555,splunk,splunk) %{_appdir}/lib/python2.5/keyword.py
%dir %attr(555,splunk,splunk) %{_appdir}/lib/python2.5/lib-dynload
%attr(555,splunk,splunk) %{_appdir}/lib/python2.5/lib-dynload/_bisect.so
%attr(555,splunk,splunk) %{_appdir}/lib/python2.5/lib-dynload/_csv.so
%attr(555,splunk,splunk) %{_appdir}/lib/python2.5/lib-dynload/_ctypes.so
%attr(555,splunk,splunk) %{_appdir}/lib/python2.5/lib-dynload/_ctypes_test.so
%attr(555,splunk,splunk) %{_appdir}/lib/python2.5/lib-dynload/_elementtree.so
%attr(555,splunk,splunk) %{_appdir}/lib/python2.5/lib-dynload/_functools.so
%attr(555,splunk,splunk) %{_appdir}/lib/python2.5/lib-dynload/_hashlib.so
%attr(555,splunk,splunk) %{_appdir}/lib/python2.5/lib-dynload/_heapq.so
%attr(555,splunk,splunk) %{_appdir}/lib/python2.5/lib-dynload/_locale.so
%attr(555,splunk,splunk) %{_appdir}/lib/python2.5/lib-dynload/_random.so
%attr(555,splunk,splunk) %{_appdir}/lib/python2.5/lib-dynload/_socket.so
%attr(555,splunk,splunk) %{_appdir}/lib/python2.5/lib-dynload/_ssl.so
%attr(555,splunk,splunk) %{_appdir}/lib/python2.5/lib-dynload/_struct.so
%attr(555,splunk,splunk) %{_appdir}/lib/python2.5/lib-dynload/_weakref.so
%attr(555,splunk,splunk) %{_appdir}/lib/python2.5/lib-dynload/array.so
%attr(555,splunk,splunk) %{_appdir}/lib/python2.5/lib-dynload/binascii.so
%attr(555,splunk,splunk) %{_appdir}/lib/python2.5/lib-dynload/bz2.so
%attr(555,splunk,splunk) %{_appdir}/lib/python2.5/lib-dynload/cPickle.so
%attr(555,splunk,splunk) %{_appdir}/lib/python2.5/lib-dynload/cStringIO.so
%attr(555,splunk,splunk) %{_appdir}/lib/python2.5/lib-dynload/collections.so
%attr(555,splunk,splunk) %{_appdir}/lib/python2.5/lib-dynload/datetime.so
%attr(555,splunk,splunk) %{_appdir}/lib/python2.5/lib-dynload/dl.so
%attr(555,splunk,splunk) %{_appdir}/lib/python2.5/lib-dynload/fcntl.so
%attr(555,splunk,splunk) %{_appdir}/lib/python2.5/lib-dynload/itertools.so
%attr(555,splunk,splunk) %{_appdir}/lib/python2.5/lib-dynload/math.so
%attr(555,splunk,splunk) %{_appdir}/lib/python2.5/lib-dynload/operator.so
%attr(555,splunk,splunk) %{_appdir}/lib/python2.5/lib-dynload/parser.so
%attr(555,splunk,splunk) %{_appdir}/lib/python2.5/lib-dynload/pyexpat.so
%attr(555,splunk,splunk) %{_appdir}/lib/python2.5/lib-dynload/resource.so
%attr(555,splunk,splunk) %{_appdir}/lib/python2.5/lib-dynload/select.so
%attr(555,splunk,splunk) %{_appdir}/lib/python2.5/lib-dynload/strop.so
%attr(555,splunk,splunk) %{_appdir}/lib/python2.5/lib-dynload/syslog.so
%attr(555,splunk,splunk) %{_appdir}/lib/python2.5/lib-dynload/termios.so
%attr(555,splunk,splunk) %{_appdir}/lib/python2.5/lib-dynload/time.so
%attr(555,splunk,splunk) %{_appdir}/lib/python2.5/lib-dynload/unicodedata.so
%attr(555,splunk,splunk) %{_appdir}/lib/python2.5/lib-dynload/zlib.so
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/linecache.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/locale.py
%dir %attr(555,splunk,splunk) %{_appdir}/lib/python2.5/logging
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/logging/__init__.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/logging/config.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/logging/handlers.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/macpath.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/macurl2path.py
%attr(555,splunk,splunk) %{_appdir}/lib/python2.5/mailbox.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/mailcap.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/markupbase.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/md5.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/mhlib.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/mimetools.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/mimetypes.py
%attr(555,splunk,splunk) %{_appdir}/lib/python2.5/mimify.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/modulefinder.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/multifile.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/mutex.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/netrc.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/new.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/nntplib.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/ntpath.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/nturl2path.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/opcode.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/optparse.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/os.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/os2emxpath.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/pdb.doc
%attr(555,splunk,splunk) %{_appdir}/lib/python2.5/pdb.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/pickle.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/pickletools.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/pipes.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/pkgutil.py
%dir %attr(555,splunk,splunk) %{_appdir}/lib/python2.5/plat-linux2
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/plat-linux2/CDROM.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/plat-linux2/DLFCN.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/plat-linux2/IN.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/plat-linux2/TYPES.py
%attr(555,splunk,splunk) %{_appdir}/lib/python2.5/plat-linux2/regen
%attr(555,splunk,splunk) %{_appdir}/lib/python2.5/platform.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/popen2.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/poplib.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/posixfile.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/posixpath.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/pprint.py
%attr(555,splunk,splunk) %{_appdir}/lib/python2.5/profile.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/pstats.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/pty.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/py_compile.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/pyclbr.py
%attr(555,splunk,splunk) %{_appdir}/lib/python2.5/pydoc.py
%attr(555,splunk,splunk) %{_appdir}/lib/python2.5/quopri.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/random.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/re.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/repr.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/rexec.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/rfc822.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/rlcompleter.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/robotparser.py
%attr(555,splunk,splunk) %{_appdir}/lib/python2.5/runpy.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/sched.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/sets.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/sgmllib.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/sha.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/shelve.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/shlex.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/shutil.py
%dir %attr(555,splunk,splunk) %{_appdir}/lib/python2.5/site-packages
%dir %attr(555,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/OpenSSL
%attr(555,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/OpenSSL/SSL.so
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/OpenSSL/__init__.py
%attr(555,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/OpenSSL/crypto.so
%attr(555,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/OpenSSL/rand.so
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/OpenSSL/tsafe.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/OpenSSL/version.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/README
%dir %attr(555,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/FtCore.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/__init__.py
%dir %attr(555,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/Attr.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/CDATASection.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/CharacterData.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/Comment.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/DOMImplementation.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/Document.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/DocumentFragment.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/DocumentType.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/Element.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/Entity.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/EntityReference.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/Event.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/FtNode.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/MessageSource.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/NamedNodeMap.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/NodeFilter.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/NodeIterator.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/NodeList.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/Notation.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/ProcessingInstruction.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/Range.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/Text.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/TreeWalker.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/__init__.py
%dir %attr(555,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/de
%dir %attr(555,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/de/LC_MESSAGES
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/de/LC_MESSAGES/4Suite.mo
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/domreg.py
%dir %attr(555,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/en_US
%dir %attr(555,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/en_US/LC_MESSAGES
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/en_US/LC_MESSAGES/4Suite.mo
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/expatbuilder.py
%dir %attr(555,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/ext
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/ext/Dom2Sax.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/ext/Printer.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/ext/Visitor.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/ext/XHtml2HtmlPrinter.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/ext/XHtmlPrinter.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/ext/__init__.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/ext/c14n.py
%dir %attr(555,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/ext/reader
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/ext/reader/HtmlLib.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/ext/reader/HtmlSax.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/ext/reader/PyExpat.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/ext/reader/Sax.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/ext/reader/Sax2.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/ext/reader/Sax2Lib.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/ext/reader/Sgmlop.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/ext/reader/__init__.py
%dir %attr(555,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/fr
%dir %attr(555,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/fr/LC_MESSAGES
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/fr/LC_MESSAGES/4Suite.mo
%dir %attr(555,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/html
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/html/GenerateHtml.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/html/HTMLAnchorElement.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/html/HTMLAppletElement.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/html/HTMLAreaElement.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/html/HTMLBRElement.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/html/HTMLBaseElement.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/html/HTMLBaseFontElement.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/html/HTMLBodyElement.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/html/HTMLButtonElement.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/html/HTMLCollection.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/html/HTMLDListElement.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/html/HTMLDOMImplementation.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/html/HTMLDirectoryElement.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/html/HTMLDivElement.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/html/HTMLDocument.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/html/HTMLElement.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/html/HTMLFieldSetElement.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/html/HTMLFontElement.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/html/HTMLFormElement.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/html/HTMLFrameElement.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/html/HTMLFrameSetElement.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/html/HTMLHRElement.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/html/HTMLHeadElement.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/html/HTMLHeadingElement.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/html/HTMLHtmlElement.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/html/HTMLIFrameElement.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/html/HTMLImageElement.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/html/HTMLInputElement.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/html/HTMLIsIndexElement.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/html/HTMLLIElement.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/html/HTMLLabelElement.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/html/HTMLLegendElement.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/html/HTMLLinkElement.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/html/HTMLMapElement.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/html/HTMLMenuElement.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/html/HTMLMetaElement.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/html/HTMLModElement.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/html/HTMLOListElement.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/html/HTMLObjectElement.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/html/HTMLOptGroupElement.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/html/HTMLOptionElement.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/html/HTMLParagraphElement.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/html/HTMLParamElement.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/html/HTMLPreElement.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/html/HTMLQuoteElement.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/html/HTMLScriptElement.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/html/HTMLSelectElement.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/html/HTMLStyleElement.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/html/HTMLTableCaptionElement.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/html/HTMLTableCellElement.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/html/HTMLTableColElement.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/html/HTMLTableElement.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/html/HTMLTableRowElement.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/html/HTMLTableSectionElement.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/html/HTMLTextAreaElement.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/html/HTMLTitleElement.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/html/HTMLUListElement.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/html/__init__.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/javadom.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/minicompat.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/minidom.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/minitraversal.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/pulldom.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/dom/xmlbuilder.py
%dir %attr(555,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/marshal
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/marshal/__init__.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/marshal/generic.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/marshal/wddx.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/ns.py
%dir %attr(555,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/parsers
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/parsers/__init__.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/parsers/expat.py
%attr(555,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/parsers/pyexpat.so
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/parsers/sgmllib.py
%attr(555,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/parsers/sgmlop.so
%dir %attr(555,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/parsers/xmlproc
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/parsers/xmlproc/__init__.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/parsers/xmlproc/_outputters.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/parsers/xmlproc/catalog.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/parsers/xmlproc/charconv.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/parsers/xmlproc/dtdparser.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/parsers/xmlproc/errors.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/parsers/xmlproc/namespace.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/parsers/xmlproc/utils.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/parsers/xmlproc/xcatalog.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/parsers/xmlproc/xmlapp.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/parsers/xmlproc/xmldtd.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/parsers/xmlproc/xmlproc.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/parsers/xmlproc/xmlutils.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/parsers/xmlproc/xmlval.py
%dir %attr(555,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/sax
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/sax/__init__.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/sax/_exceptions.py
%dir %attr(555,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/sax/drivers
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/sax/drivers/__init__.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/sax/drivers/drv_htmllib.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/sax/drivers/drv_ltdriver.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/sax/drivers/drv_ltdriver_val.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/sax/drivers/drv_pyexpat.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/sax/drivers/drv_sgmllib.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/sax/drivers/drv_sgmlop.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/sax/drivers/drv_xmldc.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/sax/drivers/drv_xmllib.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/sax/drivers/drv_xmlproc.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/sax/drivers/drv_xmlproc_val.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/sax/drivers/drv_xmltoolkit.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/sax/drivers/pylibs.py
%dir %attr(555,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/sax/drivers2
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/sax/drivers2/__init__.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/sax/drivers2/drv_htmllib.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/sax/drivers2/drv_javasax.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/sax/drivers2/drv_pyexpat.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/sax/drivers2/drv_sgmllib.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/sax/drivers2/drv_sgmlop.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/sax/drivers2/drv_sgmlop_html.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/sax/drivers2/drv_xmlproc.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/sax/expatreader.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/sax/handler.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/sax/sax2exts.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/sax/saxexts.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/sax/saxlib.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/sax/saxutils.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/sax/writer.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/sax/xmlreader.py
%dir %attr(555,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/schema
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/schema/__init__.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/schema/trex.py
%dir %attr(555,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/unicode
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/unicode/__init__.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/unicode/iso8859.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/unicode/utf8_iso.py
%dir %attr(555,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/utils
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/utils/__init__.py
%attr(555,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/utils/boolean.so
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/utils/characters.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/utils/iso8601.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/utils/qp_xml.py
%dir %attr(555,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/xpath
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/xpath/BuiltInExtFunctions.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/xpath/Context.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/xpath/Conversions.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/xpath/CoreFunctions.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/xpath/ExpandedNameWrapper.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/xpath/MessageSource.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/xpath/NamespaceNode.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/xpath/ParsedAbbreviatedAbsoluteLocationPath.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/xpath/ParsedAbbreviatedRelativeLocationPath.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/xpath/ParsedAbsoluteLocationPath.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/xpath/ParsedAxisSpecifier.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/xpath/ParsedExpr.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/xpath/ParsedNodeTest.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/xpath/ParsedPredicateList.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/xpath/ParsedRelativeLocationPath.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/xpath/ParsedStep.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/xpath/Set.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/xpath/Util.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/xpath/XPathGrammar.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/xpath/XPathParser.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/xpath/XPathParserBase.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/xpath/__init__.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/xpath/pyxpath.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/_xmlplus/xpath/yappsrt.py
%attr(555,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/apsw.so
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/fpconst.py
%dir %attr(555,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/gadfly
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/gadfly/__init__.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/gadfly/bindings.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/gadfly/client.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/gadfly/database.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/gadfly/dbapi20.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/gadfly/dbapi20error.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/gadfly/dbapi20types.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/gadfly/gfsocket.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/gadfly/grammar.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/gadfly/introspection.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/gadfly/kjParseBuild.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/gadfly/kjParser.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/gadfly/kjSet.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/gadfly/kjbuckets0.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/gadfly/kjbuckets_select.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/gadfly/operations.py
%dir %attr(555,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/gadfly/scripts
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/gadfly/scripts/__init__.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/gadfly/scripts/gfplus.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/gadfly/scripts/gfserver.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/gadfly/semantics.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/gadfly/serialize.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/gadfly/server.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/gadfly/sql.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/gadfly/sql_mar.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/gadfly/store.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/gadfly/xsdbXMLInterface.py
%dir %attr(555,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/httplib2
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/httplib2/__init__.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/httplib2/iri2uri.py
%attr(555,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/kjbuckets.so
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/log4py.py
%dir %attr(555,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/lxml
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/lxml/ElementInclude.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/lxml/__init__.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/lxml/_elementpath.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/lxml/builder.py
%attr(555,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/lxml/etree.so
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/lxml/htmlbuilder.py
%attr(555,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/lxml/objectify.so
%attr(555,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/lxml/pyclasslookup.so
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/lxml/sax.py
%dir %attr(555,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/pysqlite2
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/pysqlite2/__init__.py
%attr(555,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/pysqlite2/_sqlite.so
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/pysqlite2/dbapi2.py
%dir %attr(555,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/DateParser.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/Intersplunk.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/__init__.py
%dir %attr(555,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/appserver
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/appserver/__init__.py
%dir %attr(555,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/appserver/oxiclean
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/appserver/oxiclean/AdvancedDataManagerResource.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/appserver/oxiclean/AuthResource.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/appserver/oxiclean/AuthenticationManagerResource.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/appserver/oxiclean/CoreUIHandler.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/appserver/oxiclean/DataInputsDatabaseResource.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/appserver/oxiclean/DataInputsFifoResource.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/appserver/oxiclean/DataInputsFileResource.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/appserver/oxiclean/DataInputsNetworkResource.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/appserver/oxiclean/DataInputsResource.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/appserver/oxiclean/Dispatcher.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/appserver/oxiclean/DistributedForwardingSettingsResource.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/appserver/oxiclean/DistributedOverviewResource.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/appserver/oxiclean/DistributedReceivingSettingsResource.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/appserver/oxiclean/DistributedSearchSettingsResource.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/appserver/oxiclean/LDAPMappingResource.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/appserver/oxiclean/Query.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/appserver/oxiclean/RestartManagerResource.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/appserver/oxiclean/SearchAgent.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/appserver/oxiclean/SearchFormatter.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/appserver/oxiclean/SearchService.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/appserver/oxiclean/Template.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/appserver/oxiclean/Util.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/appserver/oxiclean/V3RestHandlers.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/appserver/oxiclean/XMLResource.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/appserver/oxiclean/__init__.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/appserver/oxiclean/html.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/appserver/oxiclean/licenseUsageManagerResource.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/appserver/oxiclean/settingsManagerResource.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/appserver/oxiclean/splunkTest.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/appserver/oxiclean/splunksManagerResource.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/appserver/oxiclean/userManagerResource.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/auth.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/bundle.py
%dir %attr(555,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/clilib
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/clilib/__init__.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/clilib/_internal.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/clilib/blobs.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/clilib/bundle.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/clilib/clean.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/clilib/cli.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/clilib/cli_common.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/clilib/control_api.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/clilib/control_exceptions.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/clilib/dbmanipulator_lib.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/clilib/deploy.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/clilib/distributed_peer.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/clilib/exports.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/clilib/getstats.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/clilib/imports.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/clilib/index.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/clilib/input_batch.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/clilib/input_exec.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/clilib/input_fifo.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/clilib/input_shared.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/clilib/input_tail.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/clilib/input_tcp.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/clilib/input_udp.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/clilib/interactive.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/clilib/literals.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/clilib/manage_auth.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/clilib/manage_boot.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/clilib/manage_config.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/clilib/manage_license.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/clilib/manage_search.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/clilib/migration.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/clilib/module.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/clilib/output_tcpout.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/clilib/output_tcpout_hack.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/clilib/package_addon.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/clilib/searchizzle.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/clilib/splunk_to_splunk.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/clilib/splunks.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/clilib/test.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/clilib/train.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/clilib/userator.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/clilib/utils_ui.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/clilib/validate.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/conf.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/csv2text.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/dcutils.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/findlogs.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/findutils.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/interactiveLearner.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/interactivedates.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/interactiveutils.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/nee.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/positionalsynonyms.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/pyLogPrintOverride.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/remote-find-logs.py
%dir %attr(555,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/rest
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/rest/__init__.py
%dir %attr(555,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/rest/external
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/rest/external/__init__.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/rest/external/test.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/rest/format.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/rest/test.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/search.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/searchResults.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/singlelineclassifier.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/sitecustomize.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/testing.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/splunk/util.py
%dir %attr(555,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/__init__.py
%dir %attr(555,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/application
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/application/__init__.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/application/app.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/application/compat.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/application/internet.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/application/service.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/application/strports.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/copyright.py
%dir %attr(555,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/cred
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/cred/__init__.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/cred/authorizer.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/cred/checkers.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/cred/credentials.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/cred/error.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/cred/identity.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/cred/pamauth.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/cred/perspective.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/cred/portal.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/cred/service.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/cred/util.py
%dir %attr(555,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/enterprise
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/enterprise/__init__.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/enterprise/adbapi.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/enterprise/reflector.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/enterprise/row.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/enterprise/sqlreflector.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/enterprise/util.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/enterprise/xmlreflector.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/im.py
%dir %attr(555,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/internet
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/internet/__init__.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/internet/abstract.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/internet/address.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/internet/app.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/internet/base.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/internet/cfreactor.py
%dir %attr(555,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/internet/cfsupport
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/internet/cfsupport/cfdate.pxi
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/internet/cfsupport/cfdecl.pxi
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/internet/cfsupport/cfrunloop.pxi
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/internet/cfsupport/cfsocket.pxi
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/internet/cfsupport/cfsupport.c
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/internet/cfsupport/cfsupport.pyx
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/internet/cfsupport/python.pxi
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/internet/default.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/internet/defer.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/internet/error.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/internet/fdesc.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/internet/glib2reactor.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/internet/gtk2reactor.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/internet/gtkreactor.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/internet/interfaces.py
%dir %attr(555,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/internet/iocpreactor
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/internet/iocpreactor/__init__.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/internet/iocpreactor/_iocp.c
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/internet/iocpreactor/abstract.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/internet/iocpreactor/client.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/internet/iocpreactor/iocpdebug.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/internet/iocpreactor/ops.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/internet/iocpreactor/proactor.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/internet/iocpreactor/server.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/internet/iocpreactor/tcp.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/internet/iocpreactor/udp.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/internet/iocpreactor/util.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/internet/kqreactor.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/internet/main.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/internet/pollreactor.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/internet/posixbase.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/internet/process.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/internet/protocol.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/internet/pyuisupport.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/internet/qtreactor.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/internet/reactor.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/internet/selectreactor.py
%dir %attr(555,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/internet/serialport
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/internet/serialport/__init__.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/internet/serialport/javaserialport.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/internet/serialport/posixserialport.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/internet/serialport/serialport.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/internet/serialport/win32serialport.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/internet/ssl.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/internet/stdio.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/internet/task.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/internet/tcp.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/internet/threadedselectreactor.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/internet/threads.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/internet/tksupport.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/internet/udp.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/internet/unix.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/internet/utils.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/internet/win32eventreactor.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/internet/wxreactor.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/internet/wxsupport.py
%dir %attr(555,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/manhole
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/manhole/__init__.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/manhole/_inspectro.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/manhole/explorer.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/manhole/gladereactor.glade
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/manhole/gladereactor.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/manhole/inspectro.glade
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/manhole/logview.glade
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/manhole/service.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/manhole/telnet.py
%dir %attr(555,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/manhole/ui
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/manhole/ui/__init__.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/manhole/ui/gtk2manhole.glade
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/manhole/ui/gtk2manhole.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/manhole/ui/gtkmanhole.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/manhole/ui/gtkrc
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/manhole/ui/pywidgets.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/manhole/ui/spelunk_gnome.py
%dir %attr(555,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/persisted
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/persisted/__init__.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/persisted/aot.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/persisted/crefutil.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/persisted/dirdbm.py
%dir %attr(555,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/persisted/journal
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/persisted/journal/__init__.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/persisted/journal/base.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/persisted/journal/picklelog.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/persisted/journal/rowjournal.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/persisted/marmalade.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/persisted/sob.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/persisted/styles.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/plugin.py
%dir %attr(555,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/plugins
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/plugins/__init__.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/plugins/dropin.cache
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/plugins/notestplugin.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/plugins/testplugin.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/plugins/twisted_ftp.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/plugins/twisted_inet.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/plugins/twisted_manhole.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/plugins/twisted_portforward.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/plugins/twisted_socks.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/plugins/twisted_telnet.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/plugins/twisted_trial.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/plugins/twisted_web.py
%dir %attr(555,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/protocols
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/protocols/__init__.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/protocols/_c_urlarg.c
%attr(555,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/protocols/_c_urlarg.so
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/protocols/basic.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/protocols/dict.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/protocols/dns.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/protocols/ethernet.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/protocols/finger.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/protocols/ftp.py
%dir %attr(555,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/protocols/gps
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/protocols/gps/__init__.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/protocols/gps/nmea.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/protocols/gps/rockwell.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/protocols/htb.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/protocols/http.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/protocols/ident.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/protocols/imap4.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/protocols/ip.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/protocols/irc.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/protocols/jabber.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/protocols/loopback.py
%dir %attr(555,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/protocols/mice
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/protocols/mice/__init__.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/protocols/mice/mouseman.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/protocols/msn.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/protocols/nntp.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/protocols/oscar.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/protocols/pcp.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/protocols/policies.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/protocols/pop3.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/protocols/portforward.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/protocols/postfix.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/protocols/raw.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/protocols/rawudp.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/protocols/shoutcast.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/protocols/sip.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/protocols/smtp.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/protocols/socks.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/protocols/stateful.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/protocols/sux.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/protocols/telnet.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/protocols/toc.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/protocols/wire.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/protocols/xmlstream.py
%dir %attr(555,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/python
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/python/__init__.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/python/_twisted_zsh_stub
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/python/compat.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/python/components.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/python/context.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/python/dispatch.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/python/dist.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/python/dxprofile.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/python/failure.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/python/filepath.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/python/finalize.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/python/formmethod.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/python/hook.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/python/htmlizer.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/python/lockfile.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/python/log.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/python/logfile.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/python/otp.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/python/plugin.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/python/procutils.py
%dir %attr(555,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/python/pymodules
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/python/pymodules/LICENSE-python.txt
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/python/pymodules/UserDictExtras.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/python/pymodules/__init__.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/python/pymodules/heapq.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/python/rebuild.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/python/reflect.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/python/release.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/python/roots.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/python/runtime.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/python/shortcut.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/python/syslog.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/python/text.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/python/threadable.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/python/threadpool.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/python/timeoutqueue.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/python/urlpath.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/python/usage.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/python/util.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/python/win32.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/python/zipstream.py
%dir %attr(555,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/python/zsh
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/python/zsh/README
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/python/zsh/_cftp
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/python/zsh/_ckeygen
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/python/zsh/_conch
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/python/zsh/_lore
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/python/zsh/_manhole
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/python/zsh/_mktap
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/python/zsh/_pyhtmlizer
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/python/zsh/_tap2deb
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/python/zsh/_tap2rpm
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/python/zsh/_tapconvert
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/python/zsh/_tkconch
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/python/zsh/_tkmktap
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/python/zsh/_trial
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/python/zsh/_twistd
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/python/zsh/_websetroot
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/python/zshcomp.py
%dir %attr(555,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/scripts
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/scripts/__init__.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/scripts/_twistw.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/scripts/htmlizer.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/scripts/manhole.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/scripts/mktap.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/scripts/tap2deb.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/scripts/tap2rpm.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/scripts/tapconvert.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/scripts/tkmktap.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/scripts/tkunzip.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/scripts/trial.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/scripts/twistd.py
%dir %attr(555,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/spread
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/spread/__init__.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/spread/banana.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/spread/cBanana.c
%attr(555,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/spread/cBanana.so
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/spread/flavors.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/spread/interfaces.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/spread/jelly.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/spread/newjelly.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/spread/pb.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/spread/publish.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/spread/refpath.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/spread/sturdy.py
%dir %attr(555,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/spread/ui
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/spread/ui/__init__.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/spread/ui/gtk2util.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/spread/ui/gtkutil.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/spread/ui/login2.glade
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/spread/ui/tktree.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/spread/ui/tkutil.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/spread/util.py
%dir %attr(555,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/tap
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/tap/__init__.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/tap/ftp.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/tap/manhole.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/tap/portforward.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/tap/socks.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/tap/telnet.py
%dir %attr(555,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/web
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/web/__init__.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/web/client.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/web/demo.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/web/distrib.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/web/domhelpers.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/web/error.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/web/google.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/web/guard.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/web/html.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/web/http.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/web/microdom.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/web/monitor.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/web/proxy.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/web/resource.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/web/rewrite.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/web/script.py
%dir %attr(555,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/web/scripts
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/web/scripts/__init__.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/web/scripts/websetroot.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/web/server.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/web/soap.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/web/static.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/web/sux.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/web/tap.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/web/trp.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/web/twcgi.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/web/util.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/web/vhost.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/web/widgets.py
%dir %attr(555,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/web/woven
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/web/woven/FlashConduit.fla
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/web/woven/FlashConduit.swf
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/web/woven/FlashConduitGlue.html
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/web/woven/WebConduit2_mozilla.js
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/web/woven/WebConduit2_msie.js
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/web/woven/WebConduitGlue.html
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/web/woven/__init__.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/web/woven/controller.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/web/woven/dirlist.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/web/woven/flashconduit.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/web/woven/form.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/web/woven/guard.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/web/woven/input.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/web/woven/interfaces.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/web/woven/model.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/web/woven/page.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/web/woven/simpleguard.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/web/woven/tapestry.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/web/woven/template.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/web/woven/utils.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/web/woven/view.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/web/woven/widgets.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/twisted/web/xmlrpc.py
%dir %attr(555,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/zope
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/zope/PUBLICATION.cfg
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/zope/README.txt
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/zope/__init__.py
%dir %attr(555,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/zope/interface
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/zope/interface/DEPENDENCIES.cfg
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/zope/interface/PUBLICATION.cfg
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/zope/interface/README.txt
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/zope/interface/SETUP.cfg
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/zope/interface/__init__.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/zope/interface/_flatten.py
%attr(555,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/zope/interface/_zope_interface_coptimizations.so
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/zope/interface/adapter.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/zope/interface/adapter.txt
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/zope/interface/advice.py
%dir %attr(555,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/zope/interface/common
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/zope/interface/common/__init__.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/zope/interface/common/idatetime.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/zope/interface/common/interfaces.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/zope/interface/common/mapping.py
%dir %attr(555,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/zope/interface/common/tests
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/zope/interface/common/tests/__init__.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/zope/interface/common/tests/basemapping.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/zope/interface/common/tests/test_idatetime.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/zope/interface/declarations.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/zope/interface/document.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/zope/interface/exceptions.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/zope/interface/human.txt
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/zope/interface/interface.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/zope/interface/interfaces.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/zope/interface/ro.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/zope/interface/verify.py
%dir %attr(555,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/zope/testing
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/zope/testing/__init__.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/zope/testing/cleanup.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/zope/testing/doctest.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/zope/testing/doctestunit.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/zope/testing/loggingsupport.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/zope/testing/loghandler.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site-packages/zope/testing/tests.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/site.py
%attr(555,splunk,splunk) %{_appdir}/lib/python2.5/smtpd.py
%attr(555,splunk,splunk) %{_appdir}/lib/python2.5/smtplib.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/sndhdr.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/socket.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/sre.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/sre_compile.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/sre_constants.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/sre_parse.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/stat.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/statvfs.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/string.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/stringold.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/stringprep.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/struct.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/subprocess.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/sunau.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/sunaudio.py
%attr(555,splunk,splunk) %{_appdir}/lib/python2.5/symbol.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/symtable.py
%attr(555,splunk,splunk) %{_appdir}/lib/python2.5/tabnanny.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/tarfile.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/telnetlib.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/tempfile.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/textwrap.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/this.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/threading.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/timeit.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/toaiff.py
%attr(555,splunk,splunk) %{_appdir}/lib/python2.5/token.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/tokenize.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/trace.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/traceback.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/tty.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/types.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/unittest.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/urllib.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/urllib2.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/urlparse.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/user.py
%attr(555,splunk,splunk) %{_appdir}/lib/python2.5/uu.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/warnings.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/wave.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/weakref.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/webbrowser.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/whichdb.py
%dir %attr(555,splunk,splunk) %{_appdir}/lib/python2.5/wsgiref
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/wsgiref/__init__.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/wsgiref/handlers.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/wsgiref/headers.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/wsgiref/simple_server.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/wsgiref/util.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/wsgiref/validate.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/xdrlib.py
%dir %attr(555,splunk,splunk) %{_appdir}/lib/python2.5/xml
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/xml/__init__.py
%dir %attr(555,splunk,splunk) %{_appdir}/lib/python2.5/xml/dom
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/xml/dom/NodeFilter.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/xml/dom/__init__.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/xml/dom/domreg.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/xml/dom/expatbuilder.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/xml/dom/minicompat.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/xml/dom/minidom.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/xml/dom/pulldom.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/xml/dom/xmlbuilder.py
%dir %attr(555,splunk,splunk) %{_appdir}/lib/python2.5/xml/etree
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/xml/etree/ElementInclude.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/xml/etree/ElementPath.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/xml/etree/ElementTree.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/xml/etree/__init__.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/xml/etree/cElementTree.py
%dir %attr(555,splunk,splunk) %{_appdir}/lib/python2.5/xml/parsers
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/xml/parsers/__init__.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/xml/parsers/expat.py
%dir %attr(555,splunk,splunk) %{_appdir}/lib/python2.5/xml/sax
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/xml/sax/__init__.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/xml/sax/_exceptions.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/xml/sax/expatreader.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/xml/sax/handler.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/xml/sax/saxutils.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/xml/sax/xmlreader.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/xmllib.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/xmlrpclib.py
%attr(444,splunk,splunk) %{_appdir}/lib/python2.5/zipfile.py

%dir %attr(555,splunk,splunk) %{_appdir}/openssl
%dir %attr(555,splunk,splunk) %{_appdir}/openssl/misc
%attr(555,splunk,splunk) %{_appdir}/openssl/misc/CA.pl
%attr(555,splunk,splunk) %{_appdir}/openssl/misc/CA.sh
%attr(555,splunk,splunk) %{_appdir}/openssl/misc/c_hash
%attr(555,splunk,splunk) %{_appdir}/openssl/misc/c_info
%attr(555,splunk,splunk) %{_appdir}/openssl/misc/c_issuer
%attr(555,splunk,splunk) %{_appdir}/openssl/misc/c_name
%attr(444,splunk,splunk) %{_appdir}/openssl/openssl.cnf

%dir %attr(555,splunk,splunk) %{_appdir}/share
%dir %attr(555,splunk,splunk) %{_appdir}/share/splunk
%dir %attr(555,splunk,splunk) %{_appdir}/share/splunk/3rdparty
%attr(444,splunk,splunk) %{_appdir}/share/splunk/3rdparty/Copyright-for-PyXML-0.8.4.txt
%attr(444,splunk,splunk) %{_appdir}/share/splunk/3rdparty/Copyright-for-Twisted-2.1.0.txt
%attr(444,splunk,splunk) %{_appdir}/share/splunk/3rdparty/Copyright-for-TwistedWeb-0.5.0.txt
%attr(444,splunk,splunk) %{_appdir}/share/splunk/3rdparty/Copyright-for-ZopeInterface-3.0.1.txt
%attr(444,splunk,splunk) %{_appdir}/share/splunk/3rdparty/Copyright-for-expat-2.0.0.txt
%attr(444,splunk,splunk) %{_appdir}/share/splunk/3rdparty/Copyright-for-fpconst-0.7.2.txt
%attr(444,splunk,splunk) %{_appdir}/share/splunk/3rdparty/Copyright-for-gadflyZip.txt
%attr(444,splunk,splunk) %{_appdir}/share/splunk/3rdparty/Copyright-for-httplib2-0.4.0.txt
%attr(444,splunk,splunk) %{_appdir}/share/splunk/3rdparty/Copyright-for-libarchive-2.2.5.txt
%attr(444,splunk,splunk) %{_appdir}/share/splunk/3rdparty/Copyright-for-libxml2-2.6.31.txt
%attr(444,splunk,splunk) %{_appdir}/share/splunk/3rdparty/Copyright-for-libxslt-1.1.22.txt
%attr(444,splunk,splunk) %{_appdir}/share/splunk/3rdparty/Copyright-for-log4py-1.3.txt
%attr(444,splunk,splunk) %{_appdir}/share/splunk/3rdparty/Copyright-for-lxml-1.3.6.txt
%attr(444,splunk,splunk) %{_appdir}/share/splunk/3rdparty/Copyright-for-lxml-elementtree-1.3.6.txt
%attr(444,splunk,splunk) %{_appdir}/share/splunk/3rdparty/Copyright-for-openldap-2.3.27.txt
%attr(444,splunk,splunk) %{_appdir}/share/splunk/3rdparty/Copyright-for-openssl-0.9.8g.txt
%attr(444,splunk,splunk) %{_appdir}/share/splunk/3rdparty/Copyright-for-pcre-7.6.txt
%attr(444,splunk,splunk) %{_appdir}/share/splunk/3rdparty/Copyright-for-xmlwrapp-0.5.0.txt
%attr(444,splunk,splunk) %{_appdir}/share/splunk/3rdparty/pyOpenSSL-0.6.tar.gz
%dir %attr(555,splunk,splunk) %{_appdir}/share/splunk/extras
%dir %attr(555,splunk,splunk) %{_appdir}/share/splunk/extras/splunkbar
%attr(444,splunk,splunk) %{_appdir}/share/splunk/extras/splunkbar/splunktoolbar.xpi
%dir %attr(555,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean
%dir %attr(555,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/dynamic
%dir %attr(555,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/dynamic/html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/dynamic/html/login.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/dynamic/html/main_ui.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/dynamic/html/service_form.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/dynamic/html/snapshot_container.html
%dir %attr(555,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/dynamic/js
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/dynamic/js/content_strings.js
%dir %attr(555,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/dynamic/xsl
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/dynamic/xsl/content_strings.xsl
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/favicon.ico
%dir %attr(555,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/a.gif
%dir %attr(555,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/calendar
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/calendar/bg_activate_small.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/calendar/btn_calNext.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/calendar/btn_calPrev.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/calendar/close.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/calendar/drop1.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/calendar/drop2.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/indent.gif
%dir %attr(555,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins
%dir %attr(555,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/arrow_contextMenu.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/arrow_contextMenu_off.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/arrow_contextMenu_on.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/arrow_contextMenu_small.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/arrow_down.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/arrow_down_small.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/arrow_down_small_on.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/arrow_sort_down.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/arrow_sort_up.gif
%dir %attr(555,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/audit
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/audit/audit_match.png
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/audit/audit_nomatch.png
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/audit/audit_unknown.png
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/bg_resultsViewControls.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/bullet_image.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/button_close.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/button_close_hi.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/button_primary_bg.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/button_secondary_bg.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/button_submit.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/dotted_horiz_bg.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/filter_tab_bg.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/filter_tab_bg_on.gif
%dir %attr(555,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/hints
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/hints/help_panel_bg.png
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/hints/help_panel_bottom_bg.png
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/hints/help_panel_bottom_left.png
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/hints/help_panel_bottom_right.png
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/hints/help_panel_button_close.png
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/hints/help_panel_button_min.png
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/hints/help_panel_page_tr.png
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/hints/help_panel_title.png
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/hints/help_panel_top_bg.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/hints/help_panel_top_bg.png
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/hints/panel_bg.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/hints/panel_title.gif
%dir %attr(555,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/histogram
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/histogram/bar_bg.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/histogram/bar_highlighted_bg.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/histogram/bar_selected_bg.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/histogram/bar_unknown_bg.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/histogram/bar_unknown_highlighted_bg.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/histogram/icon_back.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/histogram/icon_back_hi.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/histogram/icon_fwd.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/histogram/icon_fwd_hi.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/histogram/icon_snapshot.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/histogram/icon_snapshot_hi.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/histogram/icon_zoom_in.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/histogram/icon_zoom_in_hi.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/histogram/icon_zoom_out.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/histogram/icon_zoom_out_hi.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/icon_calendar.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/icon_calendar2.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/icon_circle_add.png
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/icon_circle_close.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/icon_circle_close_hi.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/icon_circle_delete.png
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/icon_close.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/icon_close_hi.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/icon_error.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/icon_filtering.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/icon_help.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/icon_layers.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/icon_maximize.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/icon_maximize_hi.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/icon_menu_closed.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/icon_menu_open.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/icon_message_error.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/icon_message_info.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/icon_minimize.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/icon_minimize_hi.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/icon_notice.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/icon_report.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/kv_mark.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/kv_mark_on.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/label_server_chooser_bg.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/logo_big_splunk.png
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/logo_big_splunk_pro.png
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/logo_splunk.png
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/menu_arrow_bg.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/menu_checkbox_bg.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/menu_checkbox_bg.png
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/menu_checkbox_boxed_bg.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/menu_checkbox_boxed_off_bg.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/menu_checkbox_green_bg.png
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/menu_radio_bg.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/msg_status_throbber.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/panel_working_bg.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/report_init_arrow.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/searchfield_bg.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/searchform_bg.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/tab_blue_off.png
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/tab_blue_on.png
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/tab_off.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/tab_on.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/tab_resultsViewControls_off.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/tab_resultsViewControls_on.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/thumb_video.png
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/time_cursor.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/time_cursor.png
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/topbar_bg.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/topology_arrow_down.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/basic/topology_arrow_right.gif
%dir %attr(555,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/arrow_contextMenu.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/arrow_contextMenu_on.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/arrow_contextMenu_small.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/arrow_down.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/arrow_down_small.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/arrow_down_small_on.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/arrow_sort_down.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/arrow_sort_up.gif
%dir %attr(555,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/audit
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/audit/audit_match.png
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/audit/audit_nomatch.png
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/audit/audit_unknown.png
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/bg_resultsViewControls.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/bullet_image.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/button_close.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/button_close_hi.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/button_primary_bg.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/button_secondary_bg.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/button_submit.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/dotted_horiz_bg.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/filter_tab_bg.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/filter_tab_bg_on.gif
%dir %attr(555,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/hints
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/hints/help_panel_bg.png
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/hints/help_panel_bottom_bg.png
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/hints/help_panel_bottom_left.png
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/hints/help_panel_bottom_right.png
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/hints/help_panel_button_close.png
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/hints/help_panel_page_tr.png
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/hints/help_panel_title.png
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/hints/help_panel_top_bg.png
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/hints/panel_bg.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/hints/panel_title.gif
%dir %attr(555,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/histogram
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/histogram/bar_bg.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/histogram/bar_highlighted_bg.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/histogram/bar_selected_bg.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/histogram/bar_unknown_bg.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/histogram/bar_unknown_highlighted_bg.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/histogram/icon_back.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/histogram/icon_back_hi.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/histogram/icon_fwd.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/histogram/icon_fwd_hi.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/histogram/icon_snapshot.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/histogram/icon_snapshot_hi.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/histogram/icon_zoom_in.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/histogram/icon_zoom_in_hi.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/histogram/icon_zoom_out.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/histogram/icon_zoom_out_hi.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/icon_calendar.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/icon_calendar2.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/icon_circle_close.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/icon_circle_close_hi.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/icon_close.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/icon_close_hi.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/icon_error.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/icon_filtering.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/icon_help.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/icon_maximize.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/icon_maximize_hi.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/icon_menu_closed.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/icon_menu_open.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/icon_message_error.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/icon_message_info.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/icon_minimize.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/icon_minimize_hi.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/icon_notice.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/kv_mark.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/kv_mark_on.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/label_server_chooser_bg.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/logo_big_splunk.png
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/logo_big_splunk_pro.png
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/logo_splunk.png
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/menu_arrow_bg.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/menu_checkbox_bg.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/menu_checkbox_bg.png
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/menu_checkbox_boxed_bg.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/menu_checkbox_boxed_off_bg.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/menu_checkbox_green_bg.png
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/menu_radio_bg.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/msg_status_throbber.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/panel_working_bg.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/report_init_arrow.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/searchfield_bg.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/searchform_bg.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/tab_black_off.png
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/tab_black_on.png
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/tab_off.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/tab_on.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/tab_resultsViewControls_off.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/tab_resultsViewControls_on.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/time_cursor.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/time_cursor.png
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/topbar_bg.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/topology_arrow_down.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/black/topology_arrow_right.gif
%dir %attr(555,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/desert
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/desert/arrow_contextMenu.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/desert/arrow_contextMenu_on.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/desert/arrow_contextMenu_small.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/desert/arrow_down.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/desert/arrow_down_small.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/desert/arrow_down_small_on.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/desert/arrow_sort_down.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/desert/arrow_sort_up.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/desert/bg_resultsViewControls.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/desert/bullet_image.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/desert/button_close.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/desert/button_close_hi.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/desert/button_primary_bg.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/desert/button_secondary_bg.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/desert/button_submit.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/desert/dotted_horiz_bg.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/desert/filter_tab_bg.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/desert/filter_tab_bg_on.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/desert/icon_calendar.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/desert/icon_calendar2.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/desert/icon_circle_close.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/desert/icon_circle_close_hi.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/desert/icon_close.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/desert/icon_close_hi.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/desert/icon_error.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/desert/icon_filtering.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/desert/icon_help.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/desert/icon_maximize.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/desert/icon_maximize_hi.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/desert/icon_menu_closed.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/desert/icon_menu_open.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/desert/icon_message_error.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/desert/icon_message_info.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/desert/icon_minimize.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/desert/icon_minimize_hi.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/desert/icon_notice.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/desert/kv_mark.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/desert/kv_mark_on.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/desert/label_server_chooser_bg.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/desert/logo_big_splunk.png
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/desert/logo_big_splunk_pro.png
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/desert/logo_splunk.png
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/desert/menu_arrow_bg.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/desert/menu_checkbox_bg.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/desert/menu_checkbox_bg.png
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/desert/menu_checkbox_boxed_bg.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/desert/menu_checkbox_boxed_off_bg.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/desert/menu_checkbox_green_bg.png
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/desert/menu_radio_bg.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/desert/msg_status_throbber.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/desert/panel_working_bg.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/desert/report_init_arrow.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/desert/searchfield_bg.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/desert/searchform_bg.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/desert/tab_black_off.png
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/desert/tab_black_on.png
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/desert/tab_off.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/desert/tab_on.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/desert/tab_resultsViewControls_off.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/desert/tab_resultsViewControls_on.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/desert/time_cursor.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/desert/time_cursor.png
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/desert/topbar_bg.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/desert/topology_arrow_down.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/skins/desert/topology_arrow_right.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/updater_free_cannot_connect.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/updater_pro_paid_login_cannot_connect.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/updater_pro_trial_login_cannot_connect.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/images/xml.gif
%dir %attr(555,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/rss
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/rss/README.txt
%dir %attr(555,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static
%dir %attr(555,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/core
%dir %attr(555,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/core/admin
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/core/admin/admin.css
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/core/admin/admin.xsl
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/core/admin/application.html
%dir %attr(555,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/core/application
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/core/application/application.css
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/core/application/application.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/core/application/application.js
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/core/application/swfobject.js
%dir %attr(555,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/core/async
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/core/async/application.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/core/async/async.css
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/core/async/async.js
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/core/async/async.xsl
%dir %attr(555,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/core/async/images
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/core/async/images/csv.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/core/async/images/json.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/core/async/images/nk.png
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/core/async/images/spl.png
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/core/async/images/u.png
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/core/async/images/xml.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/core/async/images/yaml.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/core/async/init.js
%dir %attr(555,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/core/chart
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/core/chart/chart.js
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/core/chart/chart.xsl
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/core/chart/init.js
%dir %attr(555,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/core/events
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/core/events/event.css
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/core/events/events.xsl
%dir %attr(555,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/core/jobs
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/core/jobs/init.js
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/core/jobs/jobs.js
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/core/jobs/jobs.xsl
%dir %attr(555,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/core/table
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/core/table/table.xsl
%dir %attr(555,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/core/tail
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/core/tail/application.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/core/tail/event_formatter.js
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/core/tail/flash_detect_min.js
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/core/tail/flash_tml_min.js
%dir %attr(555,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/core/tail/images
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/core/tail/images/cursor.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/core/tail/images/cursorBlink.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/core/tail/images/cursorStatic.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/core/tail/images/footerBg.png
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/core/tail/images/headerBg.png
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/core/tail/images/livesearchLogo.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/core/tail/images/livetailLogo.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/core/tail/images/searchBtn.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/core/tail/images/warning.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/core/tail/init.js
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/core/tail/request.js
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/core/tail/stream.js
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/core/tail/tail.css
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/core/tail/tail.js
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/core/tail/tail.xsl
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/core/tail/wip.txt
%dir %attr(555,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/css
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/css/admin.css
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/css/default.css
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/css/login.css
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/css/print.css
%dir %attr(555,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/css/skins
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/css/skins/basic.css
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/css/skins/black.css
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/css/skins/desert.css
%dir %attr(755,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/html/blank.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/html/help.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/html/landingpage.xml
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/html/status_404.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/html/surrounding_events.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/html/updater_free_cannot_connect.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/html/updater_pro_prod_cannot_connect.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/html/updater_pro_trial_cannot_connect.html
%dir %attr(755,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/js
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/js/admin.js
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/js/alerts.js
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/js/audit.js
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/js/charting.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/js/charting.js
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/js/dragdrop-min.js
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/js/filter.js
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/js/global.js
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/js/init.js
%dir %attr(555,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/js/jscalendar-1.0
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/js/jscalendar-1.0/calendar-green.css
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/js/jscalendar-1.0/calendar-setup.js
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/js/jscalendar-1.0/calendar.js
%dir %attr(555,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/js/jscalendar-1.0/lang
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/js/jscalendar-1.0/lang/calendar-en.js
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/js/odysseus.js
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/js/paging.js
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/js/preferences.js
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/js/profiler.js
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/js/query.js
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/js/report.js
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/js/sarissa.js
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/js/search_based_admin.js
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/js/show_source.js
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/js/stream.js
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/js/strftime.js
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/js/swfobject.js
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/js/tagging.js
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/js/timeline.js
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/js/typeahead.js
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/js/window.js
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/js/yahoo-dom-event.js
%dir %attr(555,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/swf
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/swf/charting.swf
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/swf/expressinstall.swf
%dir %attr(555,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/swf/stream
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/swf/stream/stream.swf
%dir %attr(555,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/swf/url_stream_memory_test
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/swf/url_stream_memory_test/.actionScriptProperties
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/swf/url_stream_memory_test/.project
%dir %attr(555,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/swf/url_stream_memory_test/bin
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/swf/url_stream_memory_test/bin/AC_OETags.js
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/swf/url_stream_memory_test/bin/url_stream_memory_test-debug.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/swf/url_stream_memory_test/bin/url_stream_memory_test-debug.swf
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/swf/url_stream_memory_test/bin/url_stream_memory_test.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/swf/url_stream_memory_test/bin/url_stream_memory_test.swf
%dir %attr(555,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/swf/url_stream_memory_test/html-template
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/swf/url_stream_memory_test/html-template/AC_OETags.js
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/swf/url_stream_memory_test/html-template/index.template.html
%dir %attr(755,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/xsl
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/xsl/adm.xsl
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/xsl/adm_ps.xsl
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/xsl/admin.xsl
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/xsl/datainputs.xsl
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/xsl/distributed.xsl
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/xsl/doc_rest.xsl
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/xsl/editableForm.xsl
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/xsl/ldap.xsl
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/xsl/ldapmapping.xsl
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/xsl/license.xsl
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/xsl/preferences.xsl
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/xsl/restart.xsl
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/xsl/s_common.xsl
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/xsl/s_delete_eventtype.xsl
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/xsl/s_event.xsl
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/xsl/s_metadata.xsl
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/xsl/s_progress_indicator.xsl
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/xsl/s_rename_eventtype.xsl
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/xsl/s_report.xsl
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/xsl/s_report_fields.xsl
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/xsl/s_search_fields.xsl
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/xsl/s_timeline.xsl
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/xsl/settings.xsl
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/xsl/show_source.xsl
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/xsl/splunks-v2.xsl
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/xsl/splunks.xsl
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/xsl/svg.xsl
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/xsl/typeahead.xsl
%attr(444,splunk,splunk) %{_appdir}/share/splunk/search_oxiclean/static/xsl/users.xsl
%dir %attr(555,splunk,splunk) %{_appdir}/share/splunk/testing
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/VERSION.txt
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/coding-conventions.txt
%dir %attr(555,splunk,splunk) %{_appdir}/share/splunk/testing/core
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/core/Blank.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/core/InjectedRemoteRunner.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/core/RemoteRunner.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/core/SeleniumLog.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/core/TestPrompt.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/core/TestRunner-splash.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/core/TestRunner.hta
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/core/TestRunner.html
%dir %attr(555,splunk,splunk) %{_appdir}/share/splunk/testing/core/domviewer
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/core/domviewer/butmin.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/core/domviewer/butplus.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/core/domviewer/domviewer.css
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/core/domviewer/domviewer.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/core/domviewer/selenium-domviewer.js
%dir %attr(555,splunk,splunk) %{_appdir}/share/splunk/testing/core/icons
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/core/icons/all.png
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/core/icons/continue.png
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/core/icons/continue_disabled.png
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/core/icons/pause.png
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/core/icons/pause_disabled.png
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/core/icons/selected.png
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/core/icons/step.png
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/core/icons/step_disabled.png
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/core/iedoc-core.xml
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/core/iedoc.xml
%dir %attr(555,splunk,splunk) %{_appdir}/share/splunk/testing/core/lib
%dir %attr(555,splunk,splunk) %{_appdir}/share/splunk/testing/core/lib/cssQuery
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/core/lib/cssQuery/cssQuery-p.js
%dir %attr(555,splunk,splunk) %{_appdir}/share/splunk/testing/core/lib/cssQuery/src
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/core/lib/cssQuery/src/cssQuery-level2.js
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/core/lib/cssQuery/src/cssQuery-level3.js
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/core/lib/cssQuery/src/cssQuery-standard.js
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/core/lib/cssQuery/src/cssQuery.js
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/core/lib/prototype.js
%dir %attr(555,splunk,splunk) %{_appdir}/share/splunk/testing/core/lib/scriptaculous
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/core/lib/scriptaculous/builder.js
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/core/lib/scriptaculous/controls.js
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/core/lib/scriptaculous/dragdrop.js
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/core/lib/scriptaculous/effects.js
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/core/lib/scriptaculous/scriptaculous.js
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/core/lib/scriptaculous/slider.js
%dir %attr(555,splunk,splunk) %{_appdir}/share/splunk/testing/core/scripts
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/core/scripts/find_matching_child.js
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/core/scripts/htmlutils.js
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/core/scripts/injection.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/core/scripts/injection_iframe.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/core/scripts/js2html.js
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/core/scripts/narcissus-defs.js
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/core/scripts/narcissus-exec.js
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/core/scripts/narcissus-parse.js
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/core/scripts/se2html.js
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/core/scripts/selenium-api.js
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/core/scripts/selenium-browserbot.js
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/core/scripts/selenium-browserdetect.js
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/core/scripts/selenium-commandhandlers.js
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/core/scripts/selenium-executionloop.js
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/core/scripts/selenium-logging.js
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/core/scripts/selenium-remoterunner.js
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/core/scripts/selenium-testrunner.js
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/core/scripts/selenium-version.js
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/core/scripts/user-extensions.js
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/core/scripts/user-extensions.js.sample
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/core/scripts/xmlextras.js
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/core/selenium-logo.png
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/core/selenium-test.css
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/core/selenium.css
%dir %attr(555,splunk,splunk) %{_appdir}/share/splunk/testing/core/xpath
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/core/xpath/dom.js
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/core/xpath/misc.js
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/core/xpath/xpath.js
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/index.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/install-readme.txt
%dir %attr(555,splunk,splunk) %{_appdir}/share/splunk/testing/jsunit
%dir %attr(555,splunk,splunk) %{_appdir}/share/splunk/testing/jsunit/app
%dir %attr(555,splunk,splunk) %{_appdir}/share/splunk/testing/jsunit/app/css
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/jsunit/app/css/jsUnitStyle.css
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/jsunit/app/css/readme
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/jsunit/app/emptyPage.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/jsunit/app/jsUnitCore.js
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/jsunit/app/jsUnitMockTimeout.js
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/jsunit/app/jsUnitTestManager.js
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/jsunit/app/jsUnitTestSuite.js
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/jsunit/app/jsUnitTracer.js
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/jsunit/app/jsUnitVersionCheck.js
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/jsunit/app/main-counts-errors.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/jsunit/app/main-counts-failures.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/jsunit/app/main-counts-runs.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/jsunit/app/main-counts.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/jsunit/app/main-data.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/jsunit/app/main-errors.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/jsunit/app/main-frame.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/jsunit/app/main-loader.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/jsunit/app/main-progress.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/jsunit/app/main-results.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/jsunit/app/main-status.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/jsunit/app/testContainer.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/jsunit/app/testContainerController.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/jsunit/app/xbDebug.js
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/jsunit/changelog.txt
%dir %attr(555,splunk,splunk) %{_appdir}/share/splunk/testing/jsunit/css
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/jsunit/css/jsUnitStyle.css
%dir %attr(555,splunk,splunk) %{_appdir}/share/splunk/testing/jsunit/images
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/jsunit/images/green.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/jsunit/images/logo_jsunit.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/jsunit/images/powerby-transparent.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/jsunit/images/red.gif
%dir %attr(555,splunk,splunk) %{_appdir}/share/splunk/testing/jsunit/licenses
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/jsunit/licenses/JDOM_license.txt
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/jsunit/licenses/Jetty_license.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/jsunit/licenses/MPL-1.1.txt
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/jsunit/licenses/gpl-2.txt
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/jsunit/licenses/index.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/jsunit/licenses/lgpl-2.1.txt
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/jsunit/licenses/mpl-tri-license-c.txt
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/jsunit/licenses/mpl-tri-license-html.txt
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/jsunit/readme.txt
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/jsunit/testRunner.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/jsunit/version.txt
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/readyState.xpi
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/reference.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/suite_menu.html
%dir %attr(555,splunk,splunk) %{_appdir}/share/splunk/testing/tests
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/DogFoodTestSuite.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/ErrorCheckingTestSuite.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/FailingTestSuite.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/GoogleTestSearch.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/GoogleTestSuite.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/MegaSuite.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/ShortTestSuite.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/TestAlerts.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/TestBrowserVersion.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/TestCheckUncheck.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/TestClick.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/TestClickBlankTarget.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/TestClickJavascriptHref.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/TestCommandError.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/TestComments.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/TestConfirmations.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/TestCookie.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/TestCssLocators.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/TestCursorPosition.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/TestDojoDragAndDrop.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/TestDragAndDrop.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/TestEditable.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/TestElementIndex.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/TestElementOrder.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/TestElementPresent.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/TestErrorChecking.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/TestFailingAssert.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/TestFailingVerifications.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/TestFocusOnBlur.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/TestFramesClick.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/TestFramesClickJavascriptHref.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/TestFramesNested.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/TestFramesOpen.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/TestFramesSpecialTargets.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/TestFunkEventHandling.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/TestGoBack.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/TestHighlight.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/TestHtmlSource.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/TestImplicitLocators.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/TestJS-for-loops.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/TestJS-functions.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/TestJS-if-then-else.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/TestJSSuite.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/TestJavaScriptAttributes.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/TestJavascriptParameters.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/TestLocators.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/TestModalDialog.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/TestModalDialogDialog.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/TestMultiSelect.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/TestOpen.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/TestOpenInTargetFrame.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/TestOpen_SSV_syntax.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/TestPatternMatching.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/TestPause.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/TestPrompt.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/TestProxy.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/TestQuickOpen.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/TestRefresh.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/TestSelect.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/TestSelectMultiLevelFrame.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/TestSelectWindow.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/TestStore.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/TestSubmit.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/TestSuite-UserExtensions.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/TestSuite.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/TestTextWhitespace.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/TestType.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/TestTypeRichText.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/TestUserExtensions.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/TestVerifications.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/TestVisibility.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/TestWait.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/TestWaitFor.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/TestWaitForNot.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/TestWaitInPopupWindow.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/TestXPathLocatorInXHtml.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/TestXPathLocators.html
%dir %attr(555,splunk,splunk) %{_appdir}/share/splunk/testing/tests/core
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/core/TestSuite.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/core/tail.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/default.css
%dir %attr(555,splunk,splunk) %{_appdir}/share/splunk/testing/tests/dogfood
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/dogfood/TestBaseUrl.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/dogfood/TestBreakPoint.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/dogfood/TestFailures.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/dogfood/TestPauseAndResume.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/dogfood/TestRunFailedTests.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/dogfood/TestRunSuccessfulTests.html
%dir %attr(555,splunk,splunk) %{_appdir}/share/splunk/testing/tests/dogfood/aut
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/dogfood/aut/BaseUrl1TestSuite.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/dogfood/aut/BaseUrl2TestSuite.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/dogfood/aut/FailuresTestSuite.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/dogfood/aut/PauseTestSuite.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/dogfood/aut/TestAlerts.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/dogfood/aut/TestBaseUrl1.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/dogfood/aut/TestBaseUrl2.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/dogfood/aut/TestTimeout.html
%dir %attr(555,splunk,splunk) %{_appdir}/share/splunk/testing/tests/dogfood/aut/html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/dogfood/aut/html/banner.gif
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/dogfood/aut/html/test_timeout.html
%dir %attr(555,splunk,splunk) %{_appdir}/share/splunk/testing/tests/events
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/events/TestButtonEvents.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/events/TestCheckboxEvents.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/events/TestFireEvents.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/events/TestKeyEvents.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/events/TestLinkEvents.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/events/TestMouseEvents.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/events/TestRadioEvents.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/events/TestSelectEvents.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/events/TestTextEvents.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/events/readme.txt
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/filter-tests-for-browser.js
%dir %attr(555,splunk,splunk) %{_appdir}/share/splunk/testing/tests/oxiclean
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/oxiclean/AdminTestSuite.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/oxiclean/SampleDataTestSuite.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/oxiclean/TestSuite.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/oxiclean/autorefresh.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/oxiclean/back-button.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/oxiclean/become-admin.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/oxiclean/become-free.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/oxiclean/become-power.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/oxiclean/become-user.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/oxiclean/change-group.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/oxiclean/change-user-password.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/oxiclean/create-alert-admin.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/oxiclean/create-alert-search.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/oxiclean/create-splunk.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/oxiclean/create-user.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/oxiclean/dashboards.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/oxiclean/datainput-fifo.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/oxiclean/datainput-network.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/oxiclean/distributed-search.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/oxiclean/eating-data.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/oxiclean/endless-scroller-milliseconds.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/oxiclean/endless-scroller.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/oxiclean/eventtypes.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/oxiclean/field-extractor.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/oxiclean/filters.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/oxiclean/filters_extracted.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/oxiclean/form-search.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/oxiclean/form-security.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/oxiclean/free-and-back-again.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/oxiclean/impatient_user.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/oxiclean/jsunit-global.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/oxiclean/jsunit-index.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/oxiclean/jsunit-query.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/oxiclean/live-splunk.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/oxiclean/login.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/oxiclean/permalink.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/oxiclean/preferences.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/oxiclean/report.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/oxiclean/report_links.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/oxiclean/rest-async.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/oxiclean/rest-general.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/oxiclean/searchadmin.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/oxiclean/searchlanguage.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/oxiclean/searchterm-highlighting.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/oxiclean/share-splunk.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/oxiclean/show-all-lines.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/oxiclean/show-source.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/oxiclean/sourcetype-alias.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/oxiclean/subsearches.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/oxiclean/tagging.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/oxiclean/timeline.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/oxiclean/timeline_async_update.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/oxiclean/timeline_custom_fields.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/oxiclean/timeline_merge.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/oxiclean/timeline_selection.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/oxiclean/timeline_timestamps.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/oxiclean/typeahead.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/oxiclean/typelearner.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/proxy_injection_meta_equiv_test.js
%dir %attr(555,splunk,splunk) %{_appdir}/share/splunk/testing/tests/roles
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/roles/RolesSuite.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/roles/login.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/roles/logout.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/roles/roles-admin-admin.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/roles/roles-admin-power.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/roles/roles-admin-user.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/roles/roles-setup.html
%dir %attr(555,splunk,splunk) %{_appdir}/share/splunk/testing/tests/searchlanguageCurrent
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/searchlanguageCurrent/SearchLanguageSuiteCurrent.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/searchlanguageCurrent/sL_REST_abstract.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/searchlanguageCurrent/sL_REST_addtotals.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/searchlanguageCurrent/sL_REST_admin.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/searchlanguageCurrent/sL_REST_bucket.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/searchlanguageCurrent/sL_REST_chart.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/searchlanguageCurrent/sL_REST_common.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/searchlanguageCurrent/sL_REST_convert.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/searchlanguageCurrent/sL_REST_counttable.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/searchlanguageCurrent/sL_REST_diff.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/searchlanguageCurrent/sL_REST_eval.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/searchlanguageCurrent/sL_REST_extract_kv.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/searchlanguageCurrent/sL_REST_fields.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/searchlanguageCurrent/sL_REST_fillnull.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/searchlanguageCurrent/sL_REST_format.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/searchlanguageCurrent/sL_REST_multikv.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/searchlanguageCurrent/sL_REST_page.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/searchlanguageCurrent/sL_REST_rare.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/searchlanguageCurrent/sL_REST_regex.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/searchlanguageCurrent/sL_REST_remote.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/searchlanguageCurrent/sL_REST_rename.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/searchlanguageCurrent/sL_REST_replace.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/searchlanguageCurrent/sL_REST_run.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/searchlanguageCurrent/sL_REST_savedsearch.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/searchlanguageCurrent/sL_REST_select.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/searchlanguageCurrent/sL_REST_sendemail.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/searchlanguageCurrent/sL_REST_set.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/searchlanguageCurrent/sL_REST_sort.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/searchlanguageCurrent/sL_REST_stats.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/searchlanguageCurrent/sL_REST_template.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/searchlanguageCurrent/sL_REST_timechart.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/searchlanguageCurrent/sL_REST_top.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/searchlanguageCurrent/sL_REST_where.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/searchlanguageCurrent/sL_oxi_abstract.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/searchlanguageCurrent/sL_oxi_addtotals.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/searchlanguageCurrent/sL_oxi_admin.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/searchlanguageCurrent/sL_oxi_bucket.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/searchlanguageCurrent/sL_oxi_chart.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/searchlanguageCurrent/sL_oxi_common.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/searchlanguageCurrent/sL_oxi_convert.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/searchlanguageCurrent/sL_oxi_counttable.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/searchlanguageCurrent/sL_oxi_diff.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/searchlanguageCurrent/sL_oxi_eval.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/searchlanguageCurrent/sL_oxi_extract_kv.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/searchlanguageCurrent/sL_oxi_fields.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/searchlanguageCurrent/sL_oxi_fillnull.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/searchlanguageCurrent/sL_oxi_format.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/searchlanguageCurrent/sL_oxi_multikv.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/searchlanguageCurrent/sL_oxi_page.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/searchlanguageCurrent/sL_oxi_rare.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/searchlanguageCurrent/sL_oxi_regex.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/searchlanguageCurrent/sL_oxi_rename.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/searchlanguageCurrent/sL_oxi_replace.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/searchlanguageCurrent/sL_oxi_run.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/searchlanguageCurrent/sL_oxi_savedsearch.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/searchlanguageCurrent/sL_oxi_select.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/searchlanguageCurrent/sL_oxi_sendemail.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/searchlanguageCurrent/sL_oxi_set.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/searchlanguageCurrent/sL_oxi_sort.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/searchlanguageCurrent/sL_oxi_stats.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/searchlanguageCurrent/sL_oxi_template.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/searchlanguageCurrent/sL_oxi_timechart.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/searchlanguageCurrent/sL_oxi_top.html
%attr(444,splunk,splunk) %{_appdir}/share/splunk/testing/tests/searchlanguageCurrent/sL_oxi_where.html
