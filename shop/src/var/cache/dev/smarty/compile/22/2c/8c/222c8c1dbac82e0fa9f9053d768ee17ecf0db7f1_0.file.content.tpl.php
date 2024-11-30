<?php
/* Smarty version 3.1.48, created on 2024-11-30 23:37:55
  from '/var/www/html/admin898sigruz/themes/default/template/content.tpl' */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '3.1.48',
  'unifunc' => 'content_674b93c33373e0_80324133',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
    '222c8c1dbac82e0fa9f9053d768ee17ecf0db7f1' => 
    array (
      0 => '/var/www/html/admin898sigruz/themes/default/template/content.tpl',
      1 => 1702485415,
      2 => 'file',
    ),
  ),
  'includes' => 
  array (
  ),
),false)) {
function content_674b93c33373e0_80324133 (Smarty_Internal_Template $_smarty_tpl) {
?><div id="ajax_confirmation" class="alert alert-success hide"></div>
<div id="ajaxBox" style="display:none"></div>

<div class="row">
	<div class="col-lg-12">
		<?php if ((isset($_smarty_tpl->tpl_vars['content']->value))) {?>
			<?php echo $_smarty_tpl->tpl_vars['content']->value;?>

		<?php }?>
	</div>
</div>
<?php }
}
