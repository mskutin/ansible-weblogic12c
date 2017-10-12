ADMIN_SERVER_URL = 't3://' + '{{ admin_server_hostname }}' + ':' + '{{ admin_server_port }}';

connect('{{ weblogic_admin }}', '{{ weblogic_admin_pass }}', ADMIN_SERVER_URL);

edit();
startEdit();
# applyJRF(target='{{ managed_server_name }}', domainDir='{{ domain_home }}');
cd('/')
cmo.createMachine('{{ server_hostname }}')

cd('/Machines/' + '{{ server_hostname }}' + '/NodeManager/' + '{{ server_hostname }}')
cmo.setListenAddress('{{ node_manager_listen_address }}')
cmo.setListenAddress('{{ node_manager_listen_address }}')

cd('/')
cmo.createServer('{{ managed_server_name }}')

cd('/Servers/' + '{{ managed_server_name }}')
cmo.setListenAddress('0.0.0.0')
cmo.setListenPort({{ managed_server_port }})
cmo.setMachine(getMBean('/Machines/' + '{{ server_hostname }}'))
# applyJRF(target='{{ managed_server_name }}', domainDir='{{ domain_home }}');

# applyJRF wil call save and activate
save();
activate(block='true');
disconnect();
