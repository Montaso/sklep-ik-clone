<?php
/* Smarty version 3.1.48, created on 2024-11-27 19:27:37
  from '/var/www/html/admin/themes/default/template/helpers/list/list_action_addstock.tpl' */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '3.1.48',
  'unifunc' => 'content_67476499d18f85_92304997',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
    '177b46d6ab655b5d0b8f3eac92674382816df50a' => 
    array (
      0 => '/var/www/html/admin/themes/default/template/helpers/list/list_action_addstock.tpl',
      1 => 1702485415,
      2 => 'file',
    ),
  ),
  'includes' => 
  array (
  ),
),false)) {
function content_67476499d18f85_92304997 (Smarty_Internal_Template $_smarty_tpl) {
?><a href="<?php echo call_user_func_array($_smarty_tpl->registered_plugins[ 'modifier' ][ 'escape' ][ 0 ], array( $_smarty_tpl->tpl_vars['href']->value,'html','UTF-8' ));?>
" class="edit btn btn-default" title="<?php echo $_smarty_tpl->tpl_vars['action']->value;?>
">
	<i class="icon-circle-arrow-up"></i> <?php echo $_smarty_tpl->tpl_vars['action']->value;?>

</a>
<?php }
}
