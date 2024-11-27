<?php
/* Smarty version 3.1.48, created on 2024-11-27 19:26:45
  from '/var/www/html/themes/classic/templates/customer/identity.tpl' */

/* @var Smarty_Internal_Template $_smarty_tpl */
if ($_smarty_tpl->_decodeProperties($_smarty_tpl, array (
  'version' => '3.1.48',
  'unifunc' => 'content_674764658172d6_78640196',
  'has_nocache_code' => false,
  'file_dependency' => 
  array (
    'dd1d53e92b4b636e7a8114d5e69babf9b6eef4f7' => 
    array (
      0 => '/var/www/html/themes/classic/templates/customer/identity.tpl',
      1 => 1702485415,
      2 => 'file',
    ),
  ),
  'includes' => 
  array (
  ),
),false)) {
function content_674764658172d6_78640196 (Smarty_Internal_Template $_smarty_tpl) {
$_smarty_tpl->_loadInheritance();
$_smarty_tpl->inheritance->init($_smarty_tpl, true);
?>


<?php 
$_smarty_tpl->inheritance->instanceBlock($_smarty_tpl, 'Block_2097444980674764658150e9_60625006', 'page_title');
?>


<?php 
$_smarty_tpl->inheritance->instanceBlock($_smarty_tpl, 'Block_208988368967476465816510_23481351', 'page_content');
?>

<?php $_smarty_tpl->inheritance->endChild($_smarty_tpl, 'customer/page.tpl');
}
/* {block 'page_title'} */
class Block_2097444980674764658150e9_60625006 extends Smarty_Internal_Block
{
public $subBlocks = array (
  'page_title' => 
  array (
    0 => 'Block_2097444980674764658150e9_60625006',
  ),
);
public function callBlock(Smarty_Internal_Template $_smarty_tpl) {
?>

  <?php echo call_user_func_array( $_smarty_tpl->smarty->registered_plugins[Smarty::PLUGIN_FUNCTION]['l'][0], array( array('s'=>'Your personal information','d'=>'Shop.Theme.Customeraccount'),$_smarty_tpl ) );?>

<?php
}
}
/* {/block 'page_title'} */
/* {block 'page_content'} */
class Block_208988368967476465816510_23481351 extends Smarty_Internal_Block
{
public $subBlocks = array (
  'page_content' => 
  array (
    0 => 'Block_208988368967476465816510_23481351',
  ),
);
public function callBlock(Smarty_Internal_Template $_smarty_tpl) {
?>

  <?php echo call_user_func_array( $_smarty_tpl->smarty->registered_plugins[Smarty::PLUGIN_FUNCTION]['render'][0], array( array('file'=>'customer/_partials/customer-form.tpl','ui'=>$_smarty_tpl->tpl_vars['customer_form']->value),$_smarty_tpl ) );?>

<?php
}
}
/* {/block 'page_content'} */
}
